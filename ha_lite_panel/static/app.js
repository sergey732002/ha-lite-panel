var ws = new WebSocket("ws://" + location.host + "/ws");
ws.onmessage = function(event){
 console.log(event.data);
};
