/** https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia -> Documentation about getUserMedia devices **/
const button = document.getElementById("VideoButton");
const video = document.getElementById("WebCamVideo");
let videoList = document.getElementById("videoList");

const constraints ={
  audio: false,
  video: {
    width: { min: 1024, ideal: 1280, max: 1920 },
    height: { min: 576, ideal: 720, max: 1080 }
  }
}

async function getMedia(constraints) {
  let stream = null;


  try {
    stream = await navigator.mediaDevices.getUserMedia(constraints);
    video.srcObject = stream;
    video.onloadedmetadata = function(e){
      video.play();
    }

  } catch(err) {
    console.error(err);
  }
}

/*function updateDeviceList() {
  navigator.mediaDevices.enumerateDevices()
  .then(function(devices) {
    videoList.innerHTML = "";

    devices.forEach(function(device) {
      let elem = document.createElement("li");
      let [kind, type, direction] = device.kind.match(/(\w+)(input|output)/i);

      elem.innerHTML = "<strong>" + device.label + "</strong> (" + direction + ")";
      if (type === "video") {
        videoList.appendChild(elem);
      } 

    });
  });
}*/

async function updateDeviceList(){
  let devices = null;
  
  try{
    devices = await navigator.mediaDevices.enumerateDevices()

    if(devices != null)
    {

      devices.forEach(function(device) {
        let elem = document.createElement("li");
        let [kind, type, direction] = device.kind.match(/(\w+)(input|output)/i);
  
        elem.innerHTML = "<strong>" + device.label + "</strong> (" + direction + ")";
        if (type === "video") {
          videoList.appendChild(elem);
        } 
  
      });

    }

  }
  catch(err){
    console.error(err);
  }

}


navigator.mediaDevices.ondevicechange = function(event) {
  updateDeviceList();
}

getMedia(constraints)
