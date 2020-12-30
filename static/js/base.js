$(document).ready(function() {

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
        $('nav').css('background-color', 'rgba(0, 0, 0, .35)');
      }
      atTop = true;
    }
  });

  $(".navbar-toggler").click(function() {
    if ($("nav").height() > navbarInitialHeight && atTop) {
      $('nav').css('background-color', 'rgba(0, 0, 0, .35)');
    }
    else {
      $('nav').css('background-color', 'rgba(0, 0, 0, 1)');
    }
  })
});
