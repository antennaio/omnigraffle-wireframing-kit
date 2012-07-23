$(window).load(function() {
	var i = 0;

	function fixHeight(selector) {
		h = $(document).height() - 50;
		$(selector).css({'height': h + 'px'});
	}

	fixHeight('#dragbar, #sidebar'); 

	$('#dragbar').mousedown(function(e) {
		e.preventDefault();
		$(document).mousemove(function(e) {
			if ((e.pageX > 150) && (e.pageX < 600)) {
				$('#sidebar').css("width", e.pageX + 2);
				$('#main').css("left", e.pageX + 2);
				fixHeight('#dragbar, #sidebar');
			}
		})
	});

	$(document).mouseup(function(e) {
		$(document).unbind('mousemove');
	});

    $(window).on("debouncedresize", function(e) {
        fixHeight('#dragbar, #sidebar');
    });
});
