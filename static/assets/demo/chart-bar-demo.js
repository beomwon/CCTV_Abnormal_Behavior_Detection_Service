// Set new default font family and font color to mimic Bootstrap's default stylings
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// function load(name) {
//   let xhr = new XMLHttpRequest(),
//       okStatus = document.location.protocol === "file:" ? 0 : 200;
//   xhr.open('GET', name, false);
//   xhr.overrideMimeType("text/html;charset=utf-8");//utf-8
//   xhr.send(null);
//   return xhr.status === okStatus ? xhr.responseText : null;
// }

// // let text = load("../../../occur.txt"); 

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["0801","0802", "0803", "0804", "0805", "0806", '0807',"0808", "0809", "0810", "0811", "0812", '0813',"0814", "0815", 
            "0816", "0817", "0818", '0819',"0820", "0821", "0822", "0823", "0824", '0825', "0826", '0827', "0828", '0829', "0830", '0831'],
    datasets: [{
      label: "폭행", backgroundColor: "rgba(0, 0, 255, 0.3)", borderColor: "rgba(0, 0, 255, 1)",
      data: [2, 0, 7, 10, 3, 15, 10, 3, 7, 9, 10, 13, 3, 6, 1, 4, 5, 10, 9, 0, 0, 7, 3, 13, 21, 4, 30, 6, 9, 13, 0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {unit: 'month'},
        gridLines: {display: false},
        ticks: {maxTicksLimit: 6}
      }],
      yAxes: [{
        ticks: {min: 0, max: 30, maxTicksLimit: 5},
        gridLines: {display: true}
      }],
    },
    legend: {display: false}
  }
});

var ctx = document.getElementById("myBarChart2");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["0801","0802", "0803", "0804", "0805", "0806", '0807',"0808", "0809", "0810", "0811", "0812", '0813',"0814", "0815", 
            "0816", "0817", "0818", '0819',"0820", "0821", "0822", "0823", "0824", '0825', "0826", '0827', "0828", '0829', "0830", '0831'],
    datasets: [{
      label: "실신", backgroundColor: "rgba(255, 0, 0, 0.3)", borderColor: "rgba(255, 0, 0, 1)",
      data: [20, 3, 2, 18, 6, 19, 2, 23, 21, 24, 28, 13, 5, 10, 27, 19, 5, 3, 5, 4, 20, 1, 15, 20, 19, 18, 8, 14, 13, 7, 0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {unit: 'month'},
        gridLines: {display: false},
        ticks: {maxTicksLimit: 6}
      }],
      yAxes: [{
        ticks: {min: 0, max: 30, maxTicksLimit: 5},
        gridLines: {display: true}
      }],
    },
    legend: {display: false}
  }
});

var ctx = document.getElementById("myBarChart3");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["0801","0802", "0803", "0804", "0805", "0806", '0807',"0808", "0809", "0810", "0811", "0812", '0813',"0814", "0815", 
            "0816", "0817", "0818", '0819',"0820", "0821", "0822", "0823", "0824", '0825', "0826", '0827', "0828", '0829', "0830", '0831'],
    datasets: [{
      label: "기물파손", backgroundColor: "rgba(60, 179, 113, 0.3)", borderColor: "rgba(60, 179, 113, 1)",
      data: [24, 14, 0, 13, 25, 6, 13, 27, 18, 16, 8, 15, 7, 4, 29, 22, 30, 4, 26, 8, 3, 2, 20, 23, 5, 1, 15, 27, 27, 28, 0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {unit: 'month'},
        gridLines: {display: false},
        ticks: {maxTicksLimit: 6}
      }],
      yAxes: [{
        ticks: {min: 0, max: 30, maxTicksLimit: 5},
        gridLines: {display: true}
      }],
    },
    legend: {display: false}
  }
});

var ctx = document.getElementById("myBarChart4");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["0801","0802", "0803", "0804", "0805", "0806", '0807',"0808", "0809", "0810", "0811", "0812", '0813',"0814", "0815", 
            "0816", "0817", "0818", '0819',"0820", "0821", "0822", "0823", "0824", '0825', "0826", '0827', "0828", '0829', "0830", '0831'],
    datasets: [{
      label: "계단낙상", backgroundColor: "rgba(238, 130, 238, 0.3)", borderColor: "rgba(238, 130, 238, 1)",
      data: [12, 12, 11, 19, 26, 23, 30, 7, 15, 8, 18, 8, 24, 16, 17, 7, 13, 7, 14, 30, 15, 23, 19, 20, 9, 6, 19, 22, 12, 1, 0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {unit: 'month'},
        gridLines: {display: false},
        ticks: {maxTicksLimit: 6}
      }],
      yAxes: [{
        ticks: {min: 0, max: 30, maxTicksLimit: 5},
        gridLines: {display: true}
      }],
    },
    legend: {display: false}
  }
});

var ctx = document.getElementById("myBarChart5");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["0801","0802", "0803", "0804", "0805", "0806", '0807',"0808", "0809", "0810", "0811", "0812", '0813',"0814", "0815", 
            "0816", "0817", "0818", '0819',"0820", "0821", "0822", "0823", "0824", '0825', "0826", '0827', "0828", '0829', "0830", '0831'],
    datasets: [{
      label: "무단진입", backgroundColor: "rgba(255, 165, 0, 0.3)", borderColor: "rgba(255, 165, 0, 1)",
      data: [30, 25, 21, 22, 8, 30, 12, 21, 24, 27, 13, 30, 28, 9, 3, 13, 13, 20, 24, 14, 14, 30, 23, 1, 18, 11, 1, 27, 15, 27, 0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {unit: 'month'},
        gridLines: {display: false},
        ticks: {maxTicksLimit: 6}
      }],
      yAxes: [{
        ticks: {min: 0, max: 30, maxTicksLimit: 5},
        gridLines: {display: true}
      }],
    },
    legend: {display: false}
  }
});