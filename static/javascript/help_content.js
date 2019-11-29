
function contentreset(contenttoshow) {
  document.getElementById('helpcontent').style.opacity = '0';
  if (contenttoshow == 1) {window.setTimeout(navigationcontent, 500)}
  if (contenttoshow == 2) {window.setTimeout(addtapcontent, 500)}
  if (contenttoshow == 3) {window.setTimeout(viewtapcontent, 500)}
}

function navigationcontent() {
  var contenttoshow = "Nav Content"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}

function addtapcontent() {
  var contenttoshow = "Add Tap Content"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}

function viewtapcontent() {
  var contenttoshow = "View Tap Content"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}
