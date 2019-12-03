// Function to validate signup form data before being sent via a POST request to the server
// If the function returns true the form is sent to the server for further validation
function validateSignupForm() {
  // Retrieve values from the form
  var firstName = document.getElementById("FirstName");
  var lastName = document.getElementById("LastName");
  var email = document.getElementById("Email");
  var password1 = document.getElementById("Password1")
  var password2 = document.getElementById("Password2")

  // Reset the border colour of each field in the form
  firstName.style.border = "solid 2px black";
  lastName.style.border = "solid 2px black";
  email.style.border = "solid 2px black";
  password1.style.border = "solid 2px black";
  password2.style.border = "solid 2px black";

  var letters = /^[A-Za-z]+$/;
  // If the firstName value is not solely letters
  if(firstName.value.match(letters) == null) {
    // document.getElementById('main-content').insertAdjacentHTML('afterbegin', '<p class="error">First Name Cannot Contain Numbers!</p>');
    document.getElementById('messages').innerHTML = '<p class="error message">Invalid First Name</p>';
    firstName.style.border = "solid 2px #e61f1f";
    firstName.focus();
    return false;
  }
  // If the lastName value is not solely letters
  else if(lastName.value.match(letters) == null) {
    document.getElementById('messages').innerHTML = '<p class="error message">Invalid Last Name.</p>';
    lastName.style.border = "solid 2px #e61f1f";
    lastName.focus();
    return false;
  }
  // If the password1 value is not at least 8 characters in length
  else if(password1.value.length < 8) {
    document.getElementById('messages').innerHTML = '<p class="error message">Password too short. Must be at least 8 characters.</p>';
    password1.style.border = "solid 2px #e61f1f";
    password1.focus();
    return false;
  }
  // If the password1 and password2 values do not match
  else if(password1.value !== password2.value) {
    document.getElementById('messages').innerHTML = '<p class="error message">Passwords do not match.</p>';
    password2.style.border = "solid 2px #e61f1f";
    return false
  }
  // Else submit the form
  else {
    return true;
  }
  }
