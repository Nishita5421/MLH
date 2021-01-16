
var Peer = require('simple-peer')




  var peer = new Peer({
    initiator: location.hash === '#init',
    trickle: false,
   
  })

  peer.on('signal', function (data) {
    console.log("signal")
    document.getElementById('yourId').value = JSON.stringify(data)
  })

  document.getElementById('connect').addEventListener('click', function () {
      console.log("connect button clicked")
    var otherId = JSON.parse(document.getElementById('otherId').value)
    peer.signal(otherId)
  })

  document.getElementById('send').addEventListener('click', function () {
    console.log("send button")  
    var yourMessage = document.getElementById('yourMessage').value
    var message= document.getElementById('yourMessage').textContent;
    document.getElementById("messages").textContent +='You:'+ yourMessage + '\n';   
    peer.send(yourMessage)
  })

  peer.on('data', function (data) {
      console.log("data")
      
    document.getElementById('messages').textContent +='Other:'+ data + '\n'
  })

  
