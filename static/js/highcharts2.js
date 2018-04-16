$(function () {
	var myChart = Highcharts.chart('container', {
		chart: {
			zoomType: 'xy'
		},
		title: {
			text: 'Daily Consumption'
		},
		subtitle: {
			text: 'Sunrun data 6-1-17'
		},
		xAxis: [{
			categories: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'],
			crosshair: true
		}],
		yAxis: [{ //primary axis
			title: {
				text: 'kW'
			}
		},{ // secondary axis
			title: {
				text: 'Temperature'
			},
			opposite: true
		}],
		series: [{
			name: 'Consumption',
			type: 'column',
			data: [847.73096, 1007.8808, 829.2383, 931.4151, 699.88556, 705.926, 809.8687, 855.27344, 935.1671, 1015.6099, 1224.3958, 1125.0378, 1282.0441, 1188.2356, 1045.0431, 1266.6489, 1235.3901, 1296.7838, 888.62726, 1078.9187, 1297.3693, 1145.3348, 1287.5427, 1225.4491]
		}, {
				name: 'Production',
				type: 'column',
				data: [ null, null, null, null, null, null, 28.333334, 787.3333, 922, 1061.6666, 1241.6666, 4751, 4880, 4964.3335, 4809.6665, 3290.6667, 2607.6667, 1336.6666, 866, 1083.3334, 1309.6666, 1146, 1300.6666, null]
			}, {
				name: 'Purchased',
				type: 'column',
				data: [857.39764, 1016.8808, 844.2383, 949.4151, 702.2189, 713.25934, 782.202, 73.1039, 14.442337, null, null, null, null, null, null, null, null, 15.54314, 23.206305, 2.9108303, 0, 0.95984906, 0, 1230.4491]
			},{
			name: 'Temperature',
			type: 'spline',
			yAxis: 1,
			data: [74.07, 74.52, 72.8, 72.71, 71.71, 70.92, 71.8, 74.21, 78.19, 80.26, 81.52, 82.02, 82.16, 82.01, 81.89, 81.99, 81.42, 80.44, 79.35, 77.36, 76.12, 75.77, 75.66, 74.75]
		}]
	});
});


