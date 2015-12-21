var main = function() {

  $(".img-responsive").mouseover(function() {
    $(this).addClass("show-metadata");
  });

  $(".img-responsive").mouseout(function() {
    $(this).removeClass("show-metadata");
  });

  var $lightbox = $('#lightbox');
  
  $('[data-target="#lightbox"]').on('click', function(event) {
      var $img = $(this).find('img'), 
         src = $img.data('fullsrc'),
         alt = $img.attr('alt'),
         metadata = $(this).find('.img-metadata p').clone(),
         css = {
             'maxWidth': $(window).width() - 100,
             'maxHeight': $(window).height() - 100
         };

    console.log(metadata)

     $lightbox.find('.close').addClass('hidden');
     $lightbox.find('img').attr('src', src);
     $lightbox.find('img').attr('alt', alt);
     $('.modal-metadata p').html(metadata)
     $lightbox.find('img').css(css);
  });

  $lightbox.on('shown.bs.modal', function (e) {
    var $img = $lightbox.find('img');           
    $lightbox.find('.modal-dialog').css({'width': $img.width()});
    $lightbox.find('.close').removeClass('hidden');
  });

};

$(document).ready(main);