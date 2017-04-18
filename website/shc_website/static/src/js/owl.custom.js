/*$(document).ready(function() {
	$(".owl-image").owlCarousel({
		loop : true,
		autoplay : 12000,
		items : 4,
		responsive : true,
		margin: 20,
		autoplayHoverPause : true,
		animateOut : 'slideOutUp',
		animateIn : 'slideInUp'
	});
});*/

$(document).ready(function() {
	$(".bxProdSlider").owlCarousel({
		items : 5,
	    lazyLoad : true,
	    navigation : true,
	});
});

$(document).ready(function () {
	$(".owl-image").smoothDivScroll({
		/*manualContinuousScrolling: true,
		mousewheelScrolling: "allDirections",*/
		manualContinuousScrolling: true,
		autoScrollingMode: "onStart",
		autoScrollingInterval: 10,
		autoScrollingDirection: "endlessLoopRight",
		touchScrolling: true,
	});
});