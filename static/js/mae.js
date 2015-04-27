function changeImage(img) {
  document.getElementById("gallery-main").src="/static/img/" + img;
}

function highlight(elem) {
  document.getElementById(elem).className = "gallery-thumb-highlighted";
}

function unhighlight(elem) {
  document.getElementById(elem).className = "gallery-thumb";
}
