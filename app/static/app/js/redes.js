jQuery(document).ready(function($){

$( "#ArrowRedes" ).hover(
  function() {
    $( this ).addClass('fnp-box-right');
  }, function() {
	$( this ).removeClass('fnp-box-right');
    $( this ).addClass('fnp-box-left');
  }
);

    $('.fnp-next').mouseenter(function(){
        $('.fnp-content-right').stop().animate({
            right:-20
        },300);
        $('.fnp-content-right .fnp-nav-title,.fnp-content-right .fnp-nav-link').stop().delay(300).animate({
            opacity:1
        },200)
    });
    $('.fnp-next').mouseleave(function(){
        $('.fnp-content-right').stop().animate({
            right:-175
        },300);
        $('.fnp-content-right .fnp-nav-title,.fnp-content-right .fnp-nav-link').stop().animate({
            opacity:0
        },200);
    });
});