$(document).ready(function() {
  $(window).scroll(function() {
    if ($(this).scrollTop() > 160){
      $('#navbar').addClass("sticky");
    }
    else{
      $('#navbar').removeClass("sticky");
    }
  });
});
