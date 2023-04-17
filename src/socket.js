import WebSocket from 'ws';


const ws = new WebSocket('ws://0.0.0.0:3000', {
  perMessageDeflate: false
});
console.log("running on port 3000")
ws.on('error', console.error);

ws.on('connection', (ws) => {
  ws.send('Hello!');
  console.log("hello!");
});
