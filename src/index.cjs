const { WebSocketServer } = require('ws')
const fs = require('fs')
const sockserver = new WebSocketServer({ port: 3001 })
let video = 0;
let vidData = ""
let frame = 0;
let chunkSize = 580
fs.readFile('videoEncoding.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }false,
  video = (data);
  video.split(/\r?\n/).forEach(line =>  {
    vidData+=(line+'\n');
  });
});
sockserver.on('connection', ws => {
 console.log('New client connected!')
 ws.send(vidData.slice(frame * chunkSize,frame * chunkSize + chunkSize))
 ws.on('close', () => console.log('Client has disconnected!'))
 ws.on('message', (event) =>{
  ws.send(vidData.slice(frame * chunkSize,frame * chunkSize + chunkSize))
  frame+=1
  console.log(frame)
 });
 ws.onerror = function () {
   console.log('websocket error')
 }
})