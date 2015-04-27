function changeImage(img) {
  document.getElementById("gallery-main").src="http://maeheydorn.com/wp-content/uploads/2011/03/" + img;
}

function highlight(elem) {
  document.getElementById(elem).className = "gallery-thumb-highlighted";
}

function unhighlight(elem) {
  document.getElementById(elem).className = "gallery-thumb";
}
