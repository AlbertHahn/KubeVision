//camera.js

// development logger
function log(msg) {
    logElement.innerHTML += msg + "<br>";
}

/*
Starts camera stream
with a fixed resolution for same image size 
*/
function startStream(CameraID) {
    navigator.mediaDevices.getUserMedia({
            audio: false,
            video: {
                width: 1200,
                height: 1200,
                frameRate: 30,
                deviceId: {
                    exact: CameraID
                }
            }
        }).then(stream => {
            videoElement.srcObject = stream;
        })
        .catch(err => log(err.name + ": " + err.message));
}
/*
Loops through the set of devices available for die client
Matches the ID with the device labels to identify them by name
*/


function updateDeviceList() {
    navigator.mediaDevices.enumerateDevices()
        .then(function(devices) {
            cameraOptions.innerHTML = "";
            currentDevices = devices;

            devices.forEach(function(device) {
                let elem = document.createElement("option");
                if (device.kind === "videoinput") {
                    elem.innerHTML = device.label;
                    elem.value = device.label;

                    cameraOptions.appendChild(elem)
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
function matchDevice(deviceLabel) {
    let match = [];

    currentDevices.forEach(function(device) {
        if (deviceLabel == device.label) {
            match[0] = device.deviceId;
            match[1] = device.label;
        }
    });
    return match;
}


/* Captures the video stream and draws it to a canvas, which  */
function Draw(video, context) {
    context.drawImage(video, 0, 0, videoElement.width, videoElement.height);
}

