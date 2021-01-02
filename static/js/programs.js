$(document).ready(function() {
  function openModal(program) {
    console.log("OPEN");
    $("#modal-" + program).css('display', 'block');
    $('body').css("overflow-y","hidden");
  }

  function closeModal() {
    console.log("CLOSE");
    $('.modal').css("display","none");
    $('body').css("overflow-y","visible");
  }

  function isModal(x) {
    for (let i = 0; i < x.length; i++) {

    }
  }

  $(document).click(function( e ){
    // console.log($(e.target))
    var parentsClick = []
    $(e.target).parents().each( function() {
      parentsClick.push( $(this).attr('id') )
    });
    if ( parentsClick.includes('modal-trigger') ) {
    // if ( $(e.target).parents( "modal-trigger") ) {
      if ( $(e.target).hasClass( "demobtn") ) {
        $( '#nav-' + $(e.target).data('program') + '-tab' ).click();
      }
      else {
        openModal($(e.target).closest( "#modal-trigger").data('program'));
      }
    }
    else if ( $(e.target).attr('id') ) {
      if ( $(e.target).attr('id').startsWith('modal-') ) {
        closeModal();
      }
    }
  });

  $('.close').click(function() {
    closeModal();
  });
});
