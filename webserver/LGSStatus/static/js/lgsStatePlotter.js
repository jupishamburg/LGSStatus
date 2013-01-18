(function lgsState($, document, window, lgsStateData) {
	var dailyData = [
		{
			label:'Geräte im Netz',
			data:lgsStateData.clients,
			color:'#11644D'
		},
		{
			label:'Temperatur in °C',
			data:lgsStateData.temperature,
			color:'#F24E4E'
		},
		{
			label:'Türstatus',
			data:lgsStateData.doorState,
			color:'#F78145',
			lines:{
				fill:true
			}
		}
	];

	$(document).ready(function () {
		var dayPlotter = $.plot($('#day'), dailyData, {
			xaxis:{
				mode:'time',
				ticks:10,
				minTickSize:[1, 'hour'],
				min:(new Date().getTime()) - 864e+5,
				max:(new Date().getTime()),
				timezone:'browser'
			},
			yaxis:{
				tickSize:1
			},
			legend:{
				position:'nw'
			}
		});

		$(window).resize(function () {
			dayPlotter.resize();
			dayPlotter.setupGrid();
			dayPlotter.draw();
		});
	});
})(jQuery, document, window, lgs.data);