// DOM-Elements
let videoElement = document.getElementById("video");
let logElement = document.getElementById("log");
let audioList = document.getElementById("audioList");
let videoList = document.getElementById("videoList");
const cameraOptions = document.querySelector('.custom-select');
// Variables
var currentDevices;
var canvas = document.getElementById("preview");
var context = canvas.getContext("2d")


//canvas.width = 1200
//canvas.height = 1200

/*navigator.permissions.query({name:'camera'}).then(function(result) {
  alert(result.state);
  if (result.state === 'granted') {
      console.log("granz")
  } else if (result.state === 'prompt') {
    console.log("propmt")
  } else if (result.state === 'denied') {
    console.log("denied")
  }
});*/

function log(msg) {
    logElement.innerHTML += msg + "<br>";
  }
  

function startStream(CameraID){
    navigator.mediaDevices.getUserMedia({
        audio: false,
        video: {
          
          //width: { min: 1024, ideal: 1280, max: 1920 },
          //height: { min: 576, ideal: 720, max: 1080 },
          width: 1200,
          height: 1200,
          frameRate: 30,
          deviceId: {exact: CameraID}
        }
      }).then(stream => {
          videoElement.srcObject = stream;           
        })
        .catch(err => log(err.name + ": " + err.message));
}



function updateDeviceList() {
  navigator.mediaDevices.enumerateDevices()
  .then(function(devices) {
    cameraOptions.innerHTML ="";
    currentDevices = devices;

    devices.forEach(function(device) {
      let elem = document.createElement("option");
      if (device.kind === "videoinput") {
        elem.innerHTML = device.label;
        elem.value = device.label;
 
        cameraOptions.appendChild(elem)
      } else if (device.type === "audioinput") {
        console.log("audio")
      }

    });

    console.log("works")
    let clickedDevice = matchDevice(cameraOptions.options[cameraOptions.selectedIndex].value)
    startStream(clickedDevice[0]);


  });
}

/*
Loops through current devices stored by updateDeviceList()
and matches it with the input parameter
returns deviceID
*/
function matchDevice(deviceLabel){
    let match = [];

    currentDevices.forEach(function(device) {
        if(deviceLabel == device.label){
            match[0] = device.deviceId;
            match[1] = device.label;
        }
    });
    return match;
}

cameraOptions.addEventListener('change', function() {

    let clickedDevice = matchDevice(this.value)

    startStream(clickedDevice[0])
    cameraOptions.value = clickedDevice[1]

});

function Draw(video,context){
    context.drawImage(video,0,0,videoElement.width,videoElement.height);
}

navigator.mediaDevices.ondevicechange = function(event) {
  updateDeviceList();
}

/*document.getElementById("picButton").addEventListener("click", function() {

sendFramesPerSecond(1000, 50000, 'stream')

}, false);*/





updateDeviceList();

function sendFramesPerSecond(intervalTime, maxTime, event){

  let counter= 0;
  var connectionAlive;

  let timerID = setInterval(() => {          
      counter += 1;
      Draw(videoElement, context)
      connectionAlive = sendFrames(canvas, counter, event)
      console.log("connection?: " + connectionAlive)
      if(!connectionAlive){
        clearInterval(timerID);
      } 
      console.log(counter)
  }, intervalTime)
  
  setTimeout(() => { 
      clearInterval(timerID);
  }, maxTime);

}
