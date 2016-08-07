var layer_message;
var icon_message;
var map_message;
var title_message;

function feature_drawn(){
    return shape_drawn;
}
function entered_name(form){
    return form.name.value != ""
}
function selected_layer(form){
    return form.layer.selectedIndex != 0
}
function selected_icon(form){
    return form.icon.selectedIndex != 0
}
function checkForm(form){
    var form_valid = true;
    hide_all();
    if(!feature_drawn()){
        map_message.show();
        form_valid = false;
    }
    if(!entered_name(form)) {
        title_message.show();
        form_valid = false;
    }
    if(!selected_layer(form)){
        layer_message.show();
        form_valid = false;
    }
    if(!selected_icon(form)){
        icon_message.show();
        form_valid = false;
    }
    return form_valid;
}
function showUploadImg($div,input) {
    /*
    Reads input and
    */
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $div.children().children('[name="img-preview"]').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
function hide_all(){
    layer_message.hide();
    icon_message.hide();
    title_message.hide();
    map_message.hide();
}
function expand_div($rootdiv){
    var $nextdiv = $new_img_div();
    $rootdiv.after($nextdiv);
    return $nextdiv;
}
function delete_div($rootdiv){
    $rootdiv.remove()
}
function activate_add_button($div){
    var $next_add_button = $div.children("button.add-button");
    $next_add_button.click(function(){
        expand_div($div)
    })
}
function activate_del_button($div){
    var $next_del_button = $div.children("button.del-button");
    $next_del_button.click(function(){
        delete_div($div)
    })
}
function activate_file_upload_button($div){
    $div.find('.img-input').change(function(){
        showUploadImg($div,this);
    });
}
function activate_buttons($div){
    activate_add_button($div)
    activate_del_button($div)
    activate_file_upload_button($div)
}
function $new_img_div(){
    var $retdiv = $("div.img-model").clone(true,true);
    $retdiv.show();
    $retdiv.removeClass("img-model");
    $retdiv.addClass("rootimg");

    //sets today's date as default
    var today = new Date();//today's date
    $retdiv.find('[name="month"]').attr('placeholder',today.getMonth()+1);
    $retdiv.find('[name="year"]').attr('placeholder',today.getFullYear());
    activate_buttons($retdiv);
    return $retdiv;
}
function make_img_div(img,$last_div){
    var $img_div = expand_div($last_div)
    $img_div.find('[name="month"]').val(img.month);
    $img_div.find('[name="year"]').val(img.year);
    $img_div.find('[name="img-descrip"]').val(img.description);
    $img_div.find('[name="img_id"]').val(img.id);
    $img_div.find('[name="img-preview"]').attr('src',"/static/thumbnails/"+img.filename);
    $img_div.find('[name="file"]').removeAttr('required');
    return $img_div;
}
function initalize_edit_images(){
    var $last_img_div = $("#img-start");
    ip_images.forEach(function(img){
        $last_img_div = make_img_div(img,$last_img_div);
    });
}
$(document).ready(function(){
    layer_message = $("#layer-form-issue");
    icon_message = $("#icon-form-issue");
    map_message = $("#map-form-issue");
    title_message = $("#title-form-issue");
    $("#root-add-button").click(function(){
        expand_div($("#img-start"))
    })
    initalize_edit_images();
});
