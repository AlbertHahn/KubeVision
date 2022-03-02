// DOM-Elements
let videoElement = document.getElementById("video");
let logElement = document.getElementById("log");
const cameraOptions = document.querySelector('.custom-select');
var progress= document.getElementsByClassName("progressbar")
var picButton = document.getElementById("picButton")
var loginButton = document.getElementById("loginButton")
// Variables
var currentDevices;
var canvas = document.getElementById("preview");
var context = canvas.getContext("2d")

updateDeviceList()

// Change camera stream to the selected device
cameraOptions.addEventListener('change', function() {

    let clickedDevice = matchDevice(this.value)

    startStream(clickedDevice[0])
    cameraOptions.value = clickedDevice[1]

});

// Will be executed if peripheral devices of the client have changed
navigator.mediaDevices.ondevicechange = function(event) {
    updateDeviceList();
}

// Button for sending webcam pictures as stream event to the facerecognition-server
if (picButton) {
    picButton.addEventListener("click", function() {
        picButton.disabled = true;
        sendingPictures(1000, 50000, 'stream')
    }, false);
}

// Button for sending webcam pictures as predict event to the facerecognition-server
if (loginButton) {
    loginButton.addEventListener("click", function() {
        loginButton.disabled = true;
        sendingPictures(2500, 50000, 'predict')
    }, false);
}

