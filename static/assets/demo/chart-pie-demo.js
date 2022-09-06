// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: [" ", " ", " ", " ", " "],
    datasets: [{
      data: [233, 392, 460, 463, 554],
      backgroundColor: ['rgba(0, 0, 255, 0.3)', 'rgba(255, 0, 0, 0.3)','rgba(60, 179, 113, 0.3)', 'rgba(238, 130, 238, 0.3)', 'rgba(255, 165, 0, 0.3)'],
    }],
  },
});
