const cameraOptions = document.querySelector('.custom-select');
var video = document.querySelector("#videoElement");
let streamStarted = false;

var canvas = document.getElementById("preview");
var context = canvas.getContext("2d")

canvas.width = 900;
canvas.height = 700;

context.width = canvas.width;
context.height = canvas.height;

var socket = io("ws://127.0.0.1:5000");
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected jssss!'});
});


const constraints = {
  video: {
    width: {
      min: 1280,
      ideal: 1920,
      max: 2560,
    },
    height: {
      min: 720,
      ideal: 1080,
      max: 1440
    },
  }
};

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        video.srcObject = stream;
        setInterval(function(){
          Draw(video, context);
        },10)
      })
      .catch(function (err0r) {
        console.log("Something went wrong!");
      });
  }

  const getCameraSelection = async () =>{
    const devices = await navigator.mediaDevices.enumerateDevices();
    const videoDevices = devices.filter(device => device.kind === 'videoinput');
    const options = videoDevices.map(videoDevice => {
      console.log(String(videoDevice.label))
      return `<option value="${videoDevice.deviceId}">${videoDevice.label}</option>`;
    });
    cameraOptions.innerHTML = options.join('');
  }


  

  /*const startStream = async (constraints) => {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleStream(stream);
  };

  const handleStream = (stream) => {
    video.srcObject = stream;
  };


  cameraOptions.onchange = () => {
    const updatedConstraints = {
      ...constraints,
      deviceId: {
        exact: cameraOptions.value
      }
    };
  
    startStream(updatedConstraints);
  };*/

  getCameraSelection();

  function Draw(video,context){
    context.drawImage(video,0,0,context.width,context.height);
    socket.emit('stream',canvas.toDataURL('image/webp'));
}