
function contentreset(contenttoshow) {
  document.getElementById('aboutcontent').style.opacity = '0';
  if (contenttoshow == 1) {window.setTimeout(whycontent, 500)}
  if (contenttoshow == 2) {window.setTimeout(whocontent, 500)}
  if (contenttoshow == 3) {window.setTimeout(howcontent, 500)}
  if (contenttoshow == 4) {window.setTimeout(whatcontent, 500)}
}

function whycontent() {
  var contenttoshow = "<br>" +
  "Across the world access to water is often seen as a essential human neccessity, but in some places water is may be considered a luxury." + "<br>" +
  "Water shouldn't be seen as a commercialised product, this includes water scarcity and how clean water is vital to every single individual." + "<br>" +
  "Economic, environmental, social and even political reasons can come between many of the population and this basic human right." + "<br>" +
  "We aim to provide clean and accessible water for everyone and which by no-ridiculous means by cost." + "<br>" +
  "Our focus is strongly within Churches in East Wales and Herefordshire which supply free tap-water." + "<br>" +
  "Our website will list the location of every Church residing in East Wales and Herefordshire to make sure you don't have to pay for something that should be free." + "<br>" + "<br>" +
  "- Sanjog Sambahangphe"
  document.getElementById("aboutcontent").innerHTML = contenttoshow
  document.getElementById('aboutcontent').style.opacity = '1';
}

function whocontent() {
  var contenttoshow = "<br>" + "Our team is composed of:" + "<br> <b>" +
  "Matt Barnett" + "<br>" +
  "Ronan Manning" + "<br>" +
  "Daniel Sparrow" + "<br>" +
  "Sanjog Sambahangphe" + "</b>" + "<br>" + "<br>"
  document.getElementById("aboutcontent").innerHTML = contenttoshow
  document.getElementById('aboutcontent').style.opacity = '1';
}

function howcontent() {
  var contenttoshow = "<br>" + "By creating this app, we are tackling the unnecessary and possibly harmful usage of bottled water by supplying free tap water in a simple and easy-to-understand way." + "<br>" +
  "This both has a possible positive impact on people's health (as running water is likely to be more clean than still water found in bottles) and decrease people's wasteful spending." + "<br>" + "<br>"
  document.getElementById("aboutcontent").innerHTML = contenttoshow
  document.getElementById('aboutcontent').style.opacity = '1';
}

function whatcontent() {
  var contenttoshow = "<br>" + "If you are in any way confused about the how to use this website and it's functionality there are still two things you can do." + "<br>" +
  "Firstly, you can access the help page, which is linked to just above this text, to see if that helps you navigate and use the site." + "<br>" +
  "If that doesn't help, simply send us a query using the contact us page and we'll be sure to respond to as soon as possible." + "<br>" + "<br>"
  document.getElementById("aboutcontent").innerHTML = contenttoshow
  document.getElementById('aboutcontent').style.opacity = '1';
}
