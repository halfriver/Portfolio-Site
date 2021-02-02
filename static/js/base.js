$(document).ready(function() {
  var w = window.innerWidth;
  console.log(w);

  var collapseStart = 120;
  var atTop = true;
  var navbarInitialHeight = $("nav").height();

  if ($(window).scrollTop() > collapseStart){
    $('nav').attr('style', 'padding: 5px 0px !important;');
    $('nav').css('background-color', 'rgba(0, 0, 0, 1)');
  }

  $(window).scroll(function() {
    if ($(this).scrollTop() > collapseStart){
      $('nav').attr('style', 'padding: 5px 0px !important;');
      $('nav').css('background-color', 'rgba(0, 0, 0, 1)');
      atTop = false;
    }
    else{
      if ($("nav").height() > navbarInitialHeight) {
        $('nav').attr('style', 'padding: 15px 0px !important');
        $('nav').css('background-color', 'rgba(0, 0, 0, 1)');
      } else {
        $('nav').attr('style', 'padding: 15px 0px !important');
        $('nav').css('background-color', 'rgba(0, 0, 0, .45)');
      }
      atTop = true;
    }
  });

  $(".navbar-toggler").click(function() {
    if ($("nav").height() > navbarInitialHeight && atTop) {
      $('nav').css('background-color', 'rgba(0, 0, 0, .45)');
    }
    else {
      $('nav').css('background-color', 'rgba(0, 0, 0, 1)');
    }
  });

  $(function () {
    $('[data-toggle="tooltip"]').tooltip()
  });

  if (w <= 768) {
    console.log('True')
    $('.divider').hide();
  }

  $('.foot span').text(new Date().getFullYear());
});
