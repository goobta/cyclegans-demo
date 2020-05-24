// Instance variables
var streaming = false;

var video = undefined;
var canvas = undefined;
var photo = undefined;
var cameraButton = undefined;
var uploadButton = undefined;

var sidelen = undefined;


// Functions
function init() {
  video = document.getElementById('video');
  sidelen = Math.max(video.clientWidth, video.clientHeight);

  canvas = document.getElementById('canvas');
  canvas.width = sidelen;
  canvas.height = sidelen;
  canvas.style.display = 'none';

  cameraButton = document.getElementById('cameraButton');
  cameraButton.addEventListener('click', handleCamera, false);

  uploadButton = document.getElementById('uploadButton');
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
    video.style.display = 'initial';
    canvas.style.display = 'none';

    streaming = true;
  }, false);
}

function drawToCanvas(img, width, height) {
  var context = canvas.getContext('2d');

  if(width > height) {
    var scaleFactor = height / sidelen;
  } else {
    var scaleFactor = width / sidelen;
  }

  var scaledWidth = width / scaleFactor;
  var scaledHeight = height / scaleFactor;
  var xOffset = (scaledWidth - sidelen) / 2
  var yOffset = (scaledHeight - sidelen) / 2

  context.drawImage(img, -xOffset, -yOffset, scaledWidth, scaledHeight);
}

function takePhoto() {
  drawToCanvas(video, video.videoWidth, video.videoHeight);

  video.style.display = 'none';
  canvas.style.display = 'initial';

  streaming = false;
}

function handleCamera() {
  if(streaming) {
    takePhoto();
    cameraButton.textContent = 'Take Another';
  } else {
    activate_webcam();
    cameraButton.textContent = 'Take Photo';
  }
}

// function handleUpload(event) {
//   var reader = new FileReader();

//   reader.onload = function(event) {
//     var img = new Image();

//     img.onload = function() {
//       var context = canvas.getContext('2d')
//     }
//   }
// }

// Initialize script on window load
window.addEventListener('load', init, false);