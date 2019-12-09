
function contentreset(contenttoshow) {
  document.getElementById('helpcontent').style.opacity = '0';
  if (contenttoshow == 1) {window.setTimeout(navigationcontent, 500)}
  if (contenttoshow == 2) {window.setTimeout(addtapcontent, 500)}
  if (contenttoshow == 3) {window.setTimeout(viewtapcontent, 500)}
}

function navigationcontent() {
  var contenttoshow = "<br>" +  "To navigate to the home page, please click on the title (The Water Web) located on the top-left corner of every page." + "<br>" +
  "To navigate to the any of the pages listed on the top left on the nav bar, please press their appropriate buttons and labels to be redirected to their unique pages." + "<br>" +
  "To navigate to the add-a-tap page, either press the add-a-tap button found on the home page or login using the button on the top-right of the screen to find another add-a-tap button on your profile page." + "<br>" +
  "To sign up to this website please press the sign in button on the top-right of the screen then follow the instructions on the right-hand-side of that page." + "<br>" + "<br>"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}

function addtapcontent() {
  var contenttoshow = "<br>" + "There are two methods in which you can add a tap to the map." + "<br>" +
  "The first guest-method is by navigating to the home page and following the link to the 'Add A Tap' page." + "<br>" +
  "From there you will be able to add a tap without using an account." + "<br>" +
  "Alternatively, you can also if you already have an account you can login (by using the button on the top right of every page) and add a tap from there." + "<br>" + "<br>"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}

function viewtapcontent() {
  var contenttoshow = "<br>" + "Viewing taps is relatively simple." + "<br>" +
  "Simply press the Map button on the navigation bar on the top right of the screen." + "<br>" +
  "This will take you to an easy-to-navigate integrated map where you will first see your closest maps nearest to your current location." + "<br>" + "<br>"
  document.getElementById("helpcontent").innerHTML = contenttoshow
  document.getElementById('helpcontent').style.opacity = '1';
}
