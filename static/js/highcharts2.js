$(function () {
	var myChart = Highcharts.chart('container', {
		chart: {
			type: 'line'
		},
		title: {
			text: 'Consumption'
		},
		subtitle: {
			text: 'Example'
		},
		xAxis: {
			categories: ['July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June']
		},
		yAxis: {
			title: {
				text: 'kBtu nad Gal/Occ'
			}
		},
		series: [{
			name: 'Gas',
			data: [1, 1, 1.5, 2, 4, 6, 11, 12, 8, 6, 4, 2]
		}, {
			name: 'Electric',
			data: [2.1, 2, 2.2, 2.3, 2.2, 2.4, 2.5, 2.4, 2.3, 2.2, 2.2, 2.1]
		}, {
			name: 'Water',
			data: [8, 8, 6, 5, 4, 3, 2, 2, 2, 4, 5, 6]
		}]
	});
});



