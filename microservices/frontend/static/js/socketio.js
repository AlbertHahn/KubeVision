let paragraphServer = document.getElementById("ServerStatus");
let socketServer = "http://0.0.0.0:5000"

function emitVideo(canvas){
    socket.emit('stream',canvas.toDataURL('image/webp'));
}

function establishSocketConnection(socketServer){

    var socket = io(socketServer,{ autoConnect: false});

    socket.connect();

    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected jssss!'});
        paragraphServer.innerText = "Server connection successful"
    });

    socket.on('connect_error', function() {
        console.log('Error connecting to server');
        socket.disconnect();
        paragraphServer.innerText = "Error connecting to server"
    });


}

document.getElementById("startButton").addEventListener("click", function() {

    establishSocketConnection(socketServer)

}, false);