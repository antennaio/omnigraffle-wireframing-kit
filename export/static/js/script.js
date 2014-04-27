$(window).load(function() {

	function fixSidebar() {
		h = $(window).height() - $('#header').height();

		$('#dragbar, #sidebar .menu')
			.css({'height': h + 'px'});

		if ($('#sidebar .menu ul').height() > ($(window).height() - $('#header').height())) {
			$('#sidebar .menu')
				.css('overflow-y', 'scroll');
		} else {
			$('#sidebar .menu')
				.css('overflow-y', 'auto');
		}

		$('#dragbar')
			.css('background-position', 'center ' + (($(window).height() / 2) - 40) + 'px');

	}

	fixSidebar();

	if (($.cookie('sidebar_hidden') === 'true') || (!$.cookie('sidebar_hidden'))) {
		$('#sidebar')
			.css('left', '-' + ($('#sidebar').width() - $('#dragbar').width()) + 'px')
			.data('hidden', true)
			.show();

		$('#dragbar').addClass('dragbar-hidden');

	} else {
		$('#sidebar').show();
		$('#dragbar').removeClass('dragbar-hidden');
	}

	$('#dragbar').mousedown(function(e) {
		e.preventDefault();
		if ($('#sidebar').data('hidden') === true) {
			$('#sidebar').css('left', '0').data('hidden', false);
			$('#dragbar').removeClass('dragbar-hidden');
			$.cookie('sidebar_hidden', 'false');
		} else {
			$('#sidebar')
				.css('left', '-' + ($('#sidebar').width() - $('#dragbar').width()) + 'px')
				.data('hidden', true);

			$('#dragbar').addClass('dragbar-hidden');
			$.cookie('sidebar_hidden', 'true');

		}
	});

    $(window).on('debouncedresize', function(e) {
        fixSidebar();
    });

});
