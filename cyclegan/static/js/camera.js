// Instance variables
var streaming = false;

var video = undefined;
var canvas = undefined;
var photo = undefined;
var cameraButton = undefined;

var sidelen = undefined;


// Functions
function init() {
  video = document.getElementById('video');
  sidelen = Math.max(video.clientWidth, video.clientHeight);

  canvas = document.getElementById('canvas');
  canvas.style.display = 'none';

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

function takePhoto() {
  var context = canvas.getContext('2d');

  canvas.width = sidelen;
  canvas.height = sidelen;

  if(video.videoWidth > video.videoHeight) {
    var scaleFactor = video.videoHeight / sidelen;
  } else {
    var scaleFactor = video.videoWidth / sidelen;
  }

  var scaledWidth = video.videoWidth / scaleFactor;
  var scaledHeight = video.videoHeight / scaleFactor;
  var xOffset = (scaledWidth - sidelen) / 2
  var yOffset = (scaledHeight - sidelen) / 2

  context.drawImage(video, -xOffset, -yOffset, scaledWidth, scaledHeight);

  video.style.display = 'none';
  canvas.style.display = 'initial';
}

// Initialize script on window load
window.addEventListener('load', init, false);