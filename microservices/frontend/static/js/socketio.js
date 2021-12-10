//var socket = io("http://0.0.0.0:5000");

function callConnect()
{
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected jssss!'});
        console.log("send msg")
    });
}


function emitVideo(canvas){
    socket.emit('stream',canvas.toDataURL('image/webp'));
}