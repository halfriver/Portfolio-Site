$(document).ready(function() {
  var m = new Date().getMonth();
  var d = new Date().getDate();
  if (m == 2 && d == 27) {
    $("#art-pic").css("src", "static/media/birthdayfish.png").css("title", "It's my birthday today!")
  }
  else if (m == 11 && d < 27) {
    $("#art-pic").css("src", "static/media/christmasfish.png").css("title", "Happy Holidays!")
  }
  else if ( (m == 11 && d >= 27) || (m == 0 && d < 8) ) {
    $("#art-pic").attr("src", "static/media/newyearsfish.png").css("title", "Happy New Year! あけおめ！")
  }
  else if (m == 9 && d == 31) {
    $("#art-pic").attr("src", "static/media/halloweenfish.png").css("title", "Happy Halloween!")
  }
});
