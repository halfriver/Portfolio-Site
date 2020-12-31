$(document).ready(function() {
  $( '[id$="-demo"]' ).click(function() {
    $( '#nav-' + $(this).data('program') + '-tab' ).click();
  });

  $('.card').click(function() {
    $(this).data('target')
  });
});
