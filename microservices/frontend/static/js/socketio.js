let paragraphServer = document.getElementById("ServerStatus");
//let socketServer = "http://0.0.0.0:5000"
//let socketServer = "https://labs.albert-hahn-apply.com"
//var socketServer = '{{ websocketServer }}'

console.log(socketServer)
console.log(username)

//Needs to be async for error catching
function sendFrames(canvas, counter, event){


    var socket = io(socketServer,{ autoConnect: false}, { transports: ["websocket"] });
    socket.connect();
    var alive = true;

    /*socket.on('connect', function() {
        socket.emit(event,username + "," + counter + "," + canvas.toDataURL('image/webp'))
        console.log(socket.connected);
    });*/

    socket.on('connect', function() {
        socket.emit(event,username + "," + counter + "," + canvas.toDataURL('image/webp'), (response) => {
            alive = true;
            console.log(response.status); // ok

          });
    });


    socket.on('connect_error', function() {
        console.log('Connect_error');
        paragraphServer.innerText = "Error connecting to server"
        socket.disconnect();
        connectionAlive = false;
    });

    return alive;
}

function sendingtesting(intervalTime, maxTime, event){

    let counter= 0;
    var connectionAlive;
  
    let timerID = setInterval(() => {          
        counter += 1;
        Draw(videoElement, context)


        var socket = io(socketServer,{ autoConnect: false}, { transports: ["websocket"] });
        socket.connect();
    
        /*socket.on('connect', function() {
            socket.emit(event,username + "," + counter + "," + canvas.toDataURL('image/webp'))
            console.log(socket.connected);
        });*/
    
        socket.on('connect', function() {
            socket.emit(event,username + "," + counter + "," + canvas.toDataURL('image/webp'), (response) => {
                console.log(response.status); // ok
              });
        });
    
    
        socket.on('connect_error', function() {
            console.log('Connect_error');
            paragraphServer.innerText = "Error connecting to server"
            socket.disconnect();
            clearInterval(timerID);
        });

        /*console.log("connection?: " + connectionAlive)
        if(!connectionAlive){
          clearInterval(timerID);
        } */
        console.log(counter)
    }, intervalTime)
    
    setTimeout(() => { 
        clearInterval(timerID);
    }, maxTime);
  
  }


  document.getElementById("picButton").addEventListener("click", function() {

    sendingtesting(1000, 50000, 'stream')
    
    }, false);


function establishSocketConnection(socketServer){

    var socket = io(socketServer,{ autoConnect: false});

    socket.connect();

    socket.on('connect', function() {
        socket.emit('traindata', {data: 'Client: Init training mode'});
        paragraphServer.innerText = "Server connection successful"
        socket.disconnect();
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


function sendLoginFrame(canvas){

    var socket = io(socketServer,{ autoConnect: false});
    socket.connect();

    username = "Albert"

    socket.on('connect', function() {
        socket.emit('predict',username + "," + 0 + "," + canvas.toDataURL('image/webp'))
        socket.disconnect();
    });

    socket.on('connect_error', function() {
        console.log('Error connecting to server');
        socket.disconnect();
        paragraphServer.innerText = "Error connecting to server"
    });
}

