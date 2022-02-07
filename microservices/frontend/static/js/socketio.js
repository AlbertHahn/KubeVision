let paragraphServer = document.getElementById("ServerStatus");
let progress= document.getElementById("progress")
//let socketServer = "http://0.0.0.0:5000"
//let socketServer = "https://labs.albert-hahn-apply.com"
//var socketServer = '{{ websocketServer }}'

var picButton = document.getElementById("picButton")

console.log(socketServer)
console.log(username)


function sendingtesting(intervalTime, maxTime, event){

    let counter= 0;
    var connectionAlive;
  
    let timerID = setInterval(() => {          
        counter += 1;
        Draw(videoElement, context)

        //progress.innerText = counter+ "/" + (maxTime/1000);
        progress.innerText = counter+ "/" + (maxTime/intervalTime);

        var socket = io(socketServer,{ autoConnect: false}, { transports: ["websocket"] });
        socket.connect();
    
        socket.on('connect', function() {
            socket.emit(event,username + "," + counter + "," + canvas.toDataURL('image/webp'), (response) => {
                console.log(response.status); // ok

                if ((response.status != "unknown") && (response.status != "ok"))
                {
                    document.cookie = "session_user="+response.status;
                    console.log("Cookie set to: "+"session_user="+response.status)
                    socket.disconnect();
                    location.href = profileEndpoint;

                }

              });
        });
    
    
        socket.on('connect_error', function() {
            console.log('Connect_error');
            progress.innerText = "Error connecting to server"
            socket.disconnect();
            clearInterval(timerID);
        });

        console.log(counter)
    }, intervalTime)
    
    setTimeout(() => { 
        clearInterval(timerID);
        if (event == 'stream')
        {
            startTraining(socketServer, 'traindata')
        }
    }, maxTime);


  
  }


  function startTraining(socketServer, event){

    var socket = io(socketServer,{ autoConnect: false});

    socket.connect();

    socket.on('connect', function() {
        socket.emit(event, {data: 'Client: Init training mode'}, (response) => {
            console.log(response.status); // ok
            progress.innerText = response.status;
          });
    });

    socket.on('connect_error', function() {
        console.log('Error connecting to server');
        socket.disconnect();
        progress.innerText = "Error connecting to server"
    });


}



  if(picButton){
picButton.addEventListener("click", function() {

    sendingtesting(1000, 50000, 'stream')
    
    }, false);
  }


  if(loginButton){
loginButton.addEventListener("click", function() {

    sendingtesting(2500, 50000, 'predict')

  }, false);
  }



