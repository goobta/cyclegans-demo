var width = 320;
var height = undefined;

var streaming = false;

var video = null;
var canvas = null;
var photo = null;
var startButton = null;

function startup() {
  video = document.getElementById('video');
  canvas = document.getElementById('canvas');
  photo = document.getElementById('photo');
  startButton = document.getElementById('startButton');

  navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(stream => {
      video.srcObject = stream;
      video.play();
    })
    .catch(err => console.log('Error playing video: ' + err));

  video.addEventListener('canplay', function(event) {
    if(!streaming) {
      height = video.videoHeight / (video.videoWidth / width);

      if(isNaN(height)) height = width / (4 / 3);

      video.setAttribute('width', width);
      video.setAttribute('height', height);
      canvas.setAttribute('width', width);
      canvas.setAttribute('height', height);
      streaming = true;;
    }
  }, false);
}

window.addEventListener('load', startup, false);