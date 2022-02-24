//socketio.js

function sendingtesting(intervalTime, maxTime, event) {

    let counter = 0;
    let timerID = setInterval(() => {
        counter += 1;
        Draw(videoElement, context)

        for(var i = 0; i < progress.length; i++){ progress[i].innerText = counter + "/" + (maxTime / intervalTime); };

        var socket = io(socketServer, {autoConnect: false}, {transports: ["websocket"]});
        socket.connect();

        socket.on('connect', function() {
            socket.emit(event, username + "," + counter + "," + canvas.toDataURL('image/webp'), (response) => {
                console.log(response.status); // ok

                if ((response.status != "unknown") && (response.status != "ok")) {
                    document.cookie = "session_user=" + response.status;
                    console.log("Cookie set to: " + "session_user=" + response.status)
                    socket.disconnect();
                    location.href = profileEndpoint;

                }

            });
        });


        socket.on('connect_error', function() {
            console.log('Connect_error');
            for(var i = 0; i < progress.length; i++){ progress[i].innerText = "Error connecting to server"; };
            socket.disconnect();
            clearInterval(timerID);
        });

        console.log(counter)
    }, intervalTime)

    setTimeout(() => {
        clearInterval(timerID);
        if (event == 'stream') {
            startTraining(socketServer, 'traindata')
        }
    }, maxTime);



}


function startTraining(socketServer, event) {

    var socket = io(socketServer, {
        autoConnect: false
    });

    socket.connect();

    socket.on('connect', function() {
        socket.emit(event, {
            data: 'Client: Init training mode'
        }, (response) => {
            console.log(response.status); // ok
            for(var i = 0; i < progress.length; i++){ progress[i].innerText = response.status; };
        });
    });

    socket.on('connect_error', function() {
        console.log('Error connecting to server');
        socket.disconnect();
        for(var i = 0; i < progress.length; i++){ progress[i].innerText = "Error connecting to server"; };
    });


}