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


function log(msg) {
    logElement.innerHTML += msg + "<br>";
  }
  

function startStream(CameraID){
    navigator.mediaDevices.getUserMedia({
        video: {
          width: 1024,
          height: 800,
          frameRate: 30,
          deviceId: {exact: CameraID}
        },
        audio: {
          sampleRate: 44100,
          sampleSize: 16,
          volume: 0.25
        }
      }).then(stream => {
          videoElement.srcObject = stream; 
        })
        .catch(err => log(err.name + ": " + err.message));
}

/*document.getElementById("startButton").addEventListener("click", function() {

  //let clickedDevice = matchDevice(cameraOptions.options[cameraOptions.selectedIndex].value)
  //startStream(clickedDevice[0]);

}, false);*/



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
    context.drawImage(video,0,0,canvas.width,canvas.height);
    //canvas.toDataURL('image/png')
    //photo.setAttribute('src', data);
    emitVideo(canvas)
}

navigator.mediaDevices.ondevicechange = function(event) {
  updateDeviceList();
}

document.getElementById("picButton").addEventListener("click", function() {

    Draw(videoElement, context)

}, false);

updateDeviceList();

/*setInterval(function(){
    Draw(videoElement, context);
  },10)*/

