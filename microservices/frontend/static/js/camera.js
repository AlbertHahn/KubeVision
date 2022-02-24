

function log(msg) {
    logElement.innerHTML += msg + "<br>";
}


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
Loops through 

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



function Draw(video, context) {
    context.drawImage(video, 0, 0, videoElement.width, videoElement.height);
}



function sendFramesPerSecond(intervalTime, maxTime, event) {

    let counter = 0;
    var connectionAlive;

    let timerID = setInterval(() => {
        counter += 1;
        Draw(videoElement, context)
        connectionAlive = sendFrames(canvas, counter, event)
        console.log("connection?: " + connectionAlive)
        if (!connectionAlive) {
            clearInterval(timerID);
        }
        console.log(counter)
    }, intervalTime)

    setTimeout(() => {
        clearInterval(timerID);
    }, maxTime);

}