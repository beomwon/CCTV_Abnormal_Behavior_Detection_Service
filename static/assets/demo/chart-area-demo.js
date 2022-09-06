// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["0801","0802", "0803", "0804", "0805", "0806", '0807',"0808", "0809", "0810", "0811", "0812", '0813',"0814", "0815", 
    "0816", "0817", "0818", '0819',"0820", "0821", "0822", "0823", "0824", '0825', "0826", '0827', "0828", '0829', "0830", '0831'],
    datasets: [{
      label: "all",
      lineTension: 0.3,
      backgroundColor: "rgba(0, 1, 0, 0.4)",
      borderColor: "rgba(0, 1, 0, 0.5)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(0, 1, 0, 1)",
      pointBorderColor: "rgba(0, 1, 0, 0.5)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(255, 0, 0, 1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [88, 54, 41, 82, 68, 93, 67, 81, 85, 84, 77, 79, 67, 45, 77, 65, 66, 44, 78, 56, 52, 63, 80, 77, 72, 40, 73, 96, 76, 76,  0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 100,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});


