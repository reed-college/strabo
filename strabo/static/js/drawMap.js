var shape_drawn = false;
var shapeLayer;

var def_icon = new L.Icon.Default();
var def_poly_color = '#2397EB';

function init_map(){
    /*
    Creates and configures the admin map and adds the interest points to it.
    Returns the map.
    */
    var drawMap = make_map('drawMap');
    add_tile_to(drawMap);

    var all_layers_group = make_all_layers_group(features);
    set_styles(all_layers_group);
    bind_popups(all_layers_group);
    all_layers_group.addTo(drawMap);
    return drawMap;
}

function set_draw_controls(drawMap,drawnItems){
    /*
    Sets controls which allow admin to add a polygon or a point. The control mechanics
    (options and events) allow only one feature to be placed on the map per form.
    The form control ensures that a feature was placed, so that exactly one feature will be submitted
    with the interest point.
    */

    var addControl = new L.Control.Draw({
        draw : {
          polyline: false,
          polygon: {
            shapeOptions: {
              color: def_poly_color
            }
          },
          marker:{
              icon:def_icon
          },
          circle: false,
          rectangle: false
        },

        edit: {
            featureGroup: drawnItems,
        }
    });

    var editControl = new L.Control.Draw({
      draw: false,

      edit: {
          featureGroup: drawnItems,
          edit: {
            selectedPathOptions: {
              color: 'red'
            }
          }
        }
    });

    if(edit_json){
        drawMap.addControl(editControl);
    }
    else{
        drawMap.addControl(addControl);
    }

    drawMap.on('draw:created', function (e) { //grabs layer of drawn item
        shapeLayer = e.layer;
        shape_drawn = true;
        drawnItems.addLayer(shapeLayer);

        addControl.removeFrom(drawMap);
        drawMap.addControl(editControl);
    })

    drawMap.on('draw:deleted', function (e) {
        //hackish way of finding out if there were any objects
        //that were actually deleted. Tested with leaflet 0.7.7 and leaflet-draw 0.2.3
        //probably should be retested on package upgrade
        var objs_deleted = Object.keys(e.layers._layers);
        if (objs_deleted.length > 0){
            shape_drawn = false;

            editControl.removeFrom(drawMap);
            drawMap.addControl(addControl);
        }
    })

    $("#icon-sel").change(function() {
        set_add_control_icon(addControl)
        set_marker_icon()
    });
}
function sel_text(){
    return $("#icon-sel :selected").text().trim()
}
function def_selected(){
    return sel_text() == "Select One";
}
function sel_idx(){
    return straboconfig['REVERSE_COLOR_REP'][sel_text()]
}
function sel_icon(){
    return def_selected() ? def_icon : icon_objs[sel_idx()]
}
function sel_hex_code(){
    return def_selected() ? def_poly_color : straboconfig["COLOR_HEX"][sel_idx()]
}
function set_add_control_icon(addControl){
    addControl.setDrawingOptions({
        marker: {
            icon: sel_icon()
        },
        polygon: {
          shapeOptions: {
            color: sel_hex_code()
          }
        },
    });
}
function set_marker_icon(){
    if(shape_drawn){
        if(shapeLayer instanceof L.Marker){
            shapeLayer.setIcon(sel_icon());
        }
        else{
            shapeLayer.setStyle({
                color:sel_hex_code()
            });
        }
    }
}

function init_geojson_setter(drawnItems){ // ***clarification needed*** ? what does this mean?
    if (edit_json){
        shape_drawn = true;
        shapeLayer = L.geoJson(edit_json).getLayers()[0];
        shapeLayer.addTo(drawnItems);
        shapeLayer.bindPopup("You are editing this point.").openPopup()
        set_marker_icon()
    }
    $('#upload-btn').click(function (e) {
        var JSONobject = shape_drawn ? JSON.stringify(shapeLayer.toGeoJSON()) : "";
        $('#geojson-field').attr("value", JSONobject);
    });
}

$(function(){
    var drawMap = init_map();

    var drawnItems = new L.FeatureGroup();
    drawMap.addLayer(drawnItems);
    init_geojson_setter(drawnItems)
    set_draw_controls(drawMap,drawnItems)
});
