$(function () {

    var previousScroll = 20;

    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();

        if ( scroll > 10 ) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }
  
        if (scroll >= previousScroll) {
            $('.navbar').addClass("navbar-hide");
            $('.navbar-toggler').attr("aria-expanded","false");
        
        }else if (scroll < previousScroll) {
            $('.navbar').removeClass("navbar-hide");
        }
        previousScroll = scroll;

    });
});
