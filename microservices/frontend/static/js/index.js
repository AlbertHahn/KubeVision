// DOM-Elements
let videoElement = document.getElementById("video");
let logElement = document.getElementById("log");
const cameraOptions = document.querySelector('.custom-select');
// Variables
var currentDevices;
var canvas = document.getElementById("preview");
var context = canvas.getContext("2d")

//let paragraphServer = document.getElementById("ServerStatus");
var progress= document.getElementsByClassName("progressbar")
var picButton = document.getElementById("picButton")
var loginButton = document.getElementById("loginButton")

cameraOptions.addEventListener('change', function() {

    let clickedDevice = matchDevice(this.value)

    startStream(clickedDevice[0])
    cameraOptions.value = clickedDevice[1]

});

navigator.mediaDevices.ondevicechange = function(event) {
    updateDeviceList();
}

updateDeviceList()

if (picButton) {
    picButton.addEventListener("click", function() {
        picButton.disabled = true;
        sendingtesting(1000, 50000, 'stream')
    }, false);
}


if (loginButton) {
    loginButton.addEventListener("click", function() {
        loginButton.disabled = true;
        sendingtesting(2500, 50000, 'predict')
    }, false);
}

