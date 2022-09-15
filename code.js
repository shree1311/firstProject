// path -- string specifying URL to which data request is sent
// callback -- function called by JavaScript when response is received 
function ajaxGetRequest(path, callback) {
  let request = new XMLHttpRequest(); 
  request.onreadystatechange = function() {
    if (this.readyState===4 && this.status ===200) 
      {callback(this.response);
    }   
  }
  request.open("GET", path);
  request.send(); 
}

// path -- string specifying URL to which data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received 
function ajaxPostRequest(path, data, callback) {
  let request = new XMLHttpRequest(); 
  request.onreadystatechange = function() {
  if (this.readyState===4 && this.status ===200) { 
    callback(this.response);
    } 
  }
  request.open("POST", path);
  request.send(data); 
}

function getData(){
  ajaxGetRequest("/barChart",barChart);
  ajaxGetRequest("/pieChart",pieChart);
}

function barChart(response){
  let bar = document.getElementById("barChart");
  let data = JSON.parse(response);
  Plotly.newPlot(bar,data);
}

function pieChart(response){
  let pie = document.getElementById("pieChart");
  let data = JSON.parse(response);
  Plotly.newPlot(pie,data);
}

function textboxval(){
  let textBox = document.getElementById("input");
  let message = textBox.value;
  //textBox.value = '';
  let data = JSON.stringify({"message":message});
  ajaxPostRequest("/linechart",data,lineChart);
}

function lineChart(response){
  let line = document.getElementById("lineChart");
  let data = JSON.parse(response);
  Plotly.newPlot(line,data)
}
