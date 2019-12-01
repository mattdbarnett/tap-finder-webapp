
function contentreset(contenttoshow) {
  document.getElementById('helpcontent').style.opacity = '0';
  if (contenttoshow == 1) {window.setTimeout(navigationcontent, 500)}
  if (contenttoshow == 2) {window.setTimeout(addtapcontent, 500)}
  if (contenttoshow == 3) {window.setTimeout(viewtapcontent, 500)}
}

function navigationcontent() {
  var contenttoshow = "To navigate to the home page, please click on the title (The Water Web) located on the top-left corner of every page."
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}

function addtapcontent() {
  var contenttoshow = "There are two methods in which you can add a tap to the map. The first guest-method is by navigating to the home page and following the link to the 'Add A Tap' page. From there you will be able to add a tap without using an account. Alternatively, you can also if you already have an account you can login (by using the button on the top right of every page) and add a tap from there."
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}

function viewtapcontent() {
  var contenttoshow = "View Tap Content"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}
