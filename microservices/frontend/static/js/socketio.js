//socketio.js

/*
Main function for sending pictures to the facerecognition-service 
Takes parameter in for time intervals of sending pictures
MaxTime for maximal duration of the process
Event on which socket.io eventlistener it should send the pictures
*/

function sendingPictures(intervalTime, maxTime, event) {

    
    let counter = 0;

    // Sets timer for the function
    let timerID = setInterval(() => {
        counter += 1;
        Draw(videoElement, context)

        // Updates the progress screen for the user interface
        for(var i = 0; i < progress.length; i++){ progress[i].innerText = counter + "/" + (maxTime / intervalTime); };

        // Initializes the socketSever, which were injected through jinja2
        var socket = io(socketServer, {autoConnect: false}, {transports: ["websocket"]});
        socket.connect();

        // Sends data in form of username, counter and image to an endpoint
        socket.on('connect', function() {
            socket.emit(event, username + "," + counter + "," + canvas.toDataURL('image/webp'), (response) => {
                console.log(response.status); // ok

                // If the facerecognition-server response with a username the user will be logged in
                if ((response.status != "unknown") && (response.status != "ok")) {
                    // Sets the cookie to the predicted user of the facerecognition-service
                    document.cookie = "session_user=" + response.status;
                    console.log("Cookie set to: " + "session_user=" + response.status)
                    socket.disconnect();
                    location.href = homeEndpoint;

                }

            });
        });


        // If an error occurs drop socket.io connection and update user interface
        socket.on('connect_error', function() {
            console.log('Connect_error');
            for(var i = 0; i < progress.length; i++){ progress[i].innerText = "Error connecting to server"; };
            socket.disconnect();
            // Stop interval function
            clearInterval(timerID);
        });
        console.log(counter)
    }, intervalTime)

    // Cancel function if time progressed to maxTime 
    setTimeout(() => {
        clearInterval(timerID);

        // If event stream send msg. object to facerecognition-service to start a training of the received data
        if (event == 'stream') {
            startTraining(socketServer, 'traindata')
        }
    }, maxTime);



}

/*
Main purpose of this function is the trigger event of the facerecognition-service traindata
Will be executed for triggering the event traindata

*/

function startTraining(socketServer, event) {

    // Initialize Socket.IO server object
    var socket = io(socketServer, {
        autoConnect: false
    });

    // Connect to server
    socket.connect();

    // Trigger listener to train datasets
    socket.on('connect', function() {
        socket.emit(event, {
            data: 'Client: Init training mode'
        }, (response) => {
            console.log(response.status); // ok
            for(var i = 0; i < progress.length; i++){ progress[i].innerText = response.status; };
        });
    });

    // Throw exception
    socket.on('connect_error', function() {
        console.log('Error connecting to server');
        socket.disconnect();
        for(var i = 0; i < progress.length; i++){ progress[i].innerText = "Error connecting to server"; };
    });


}