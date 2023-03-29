const canvas = document.getElementById("lebensmittelLadesymbol");
const ctx = canvas.getContext("2d");
let start = 0;

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = "#4CAF50";
  ctx.lineWidth = 20;
  ctx.lineCap = "round";

  ctx.beginPath();
  ctx.arc(canvas.width / 2, canvas.height / 2, 100, start, start + Math.PI * 1.5);
  ctx.stroke();

  start += 0.1;
  requestAnimationFrame(draw);
}

function startAnimation() {
  canvas.style.display = "block";
  draw();
}

function stopAnimation() {
  canvas.style.display = "none";
  cancelAnimationFrame(draw);
}
