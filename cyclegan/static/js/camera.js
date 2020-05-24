// Hyper parameters
const sideLen = 320;

// Instance variables
var streaming = false;

var video = undefined;
var canvas = undefined;
var photo = undefined;
var cameraButton = undefined;


// Functions
function init() {
  video = document.getElementById('video');
  canvas = document.getElementById('canvas');
  photo = document.getElementById('photo');
  cameraButton = document.getElementById('cameraButton');

  cameraButton.addEventListener('click', activate_webcam, false);
}

function activate_webcam() {
  if(streaming) return;

  navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(stream => {
      video.srcObject = stream;
      video.play();
    })
    .catch(err => console.log('Error playing video: ' + err));

  video.addEventListener('canplay', function(event) {
    streaming = true;;
  }, false);
}


// Initialize script on window load
window.addEventListener('load', init, false);