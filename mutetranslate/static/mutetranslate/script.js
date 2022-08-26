const URL = "https://teachablemachine.withgoogle.com/models/_zjVBdiwg/";
let model, webcam, ctx, labelContainer, maxPredictions;

async function init() {
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";

  model = await tmPose.load(modelURL, metadataURL);
  maxPredictions = model.getTotalClasses();

  const size = 350;
  const flip = true;
  webcam = new tmPose.Webcam(350, size, flip);
  await webcam.setup();
  await webcam.play();
  window.requestAnimationFrame(loop);

  const canvas = document.getElementById("canvas");
  canvas.width = size; canvas.height = size;
  ctx = canvas.getContext("2d");
  labelContainer = document.getElementById("label-container");
  for (let i = 0; i < maxPredictions; i++) {
    labelContainer.appendChild(document.createElement("div"));
  }
}

async function loop(timestamp) {
  webcam.update();
  await predict();
  window.requestAnimationFrame(loop);
}

async function predict() {
  const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
  const prediction = await model.predict(posenetOutput);
//  let maximum = 0
//  for (let i = 0; i < maxPredictions; i++) {
//      labelContainer.childNodes[i].innerHTML = " "
//  }
  let temp = 0;
  for (let i = 0; i < maxPredictions; i++) {
//    if (prediction[i].probability > maximum)  {
//      maximum = prediction[i].probability
      if (prediction[i].probability.toFixed(2) > temp) {
        temp = prediction[i].probability.toFixed(2);
        const classPrediction = prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
      } else {
        continue
      }
//    }
  }

  drawPose(pose);
}

function drawPose(pose) {
  if (webcam.canvas) {
    ctx.drawImage(webcam.canvas, 0, 0);
    if (pose) {
      const minPartConfidence = 0.95;
      tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
      tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
    }
  }
}