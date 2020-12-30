function openModal(tag) {
  document.getElementById("modal-" + tag).style.display = "block";
  console.log("modal-" + tag)
  $(document).find('.carousel-indicators').attr('hidden', true);
}

function currentSlide(n, tag) {
  showSlides(slideIndex = n, tag);
}

function plusSlides(n, tag) {
  showSlides(slideIndex += n, tag);
}

function showSlides(n, tag) {
  var i;
  var slides = document.getElementsByClassName("mySlides-" + tag);
  console.log(slides)
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

$(document).ready(function() {
  $('.card').hover(
    function() {
      $(this).find('.card-img-overlay').removeAttr('hidden');
      console.log($(this).find('.card-img-overlay').data('description'));
    },
    function() {
      $(this).find('.card-img-overlay').attr('hidden', true);
    }
  );

  // var slideIndex = 1;
  // showSlides(slideIndex);


  $('.close').click(function() {
    $(this).parent().css("display","none");
    $(document).find('.carousel-indicators').removeAttr('hidden')
  });
});
