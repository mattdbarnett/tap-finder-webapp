function validateSignupForm() {
  var firstName = document.getElementById("FirstName");
  var lastName = document.getElementById("LastName");
  var email = document.getElementById("Email");
  var password1 = document.getElementById("Password1")
  var password2 = document.getElementById("Password2")

  firstName.style.border = "solid 2px black";
  lastName.style.border = "solid 2px black";
  email.style.border = "solid 2px black";
  password1.style.border = "solid 2px black";
  password2.style.border = "solid 2px black";

  var letters = /^[A-Za-z]+$/;
  if(firstName.value.match(letters) == null) {
    // document.getElementById('main-content').insertAdjacentHTML('afterbegin', '<p class="error">First Name Cannot Contain Numbers!</p>');
    document.getElementById('messages').innerHTML = '<p class="error message">Invalid First Name</p>';
    firstName.style.border = "solid 2px #e61f1f";
    firstName.focus();
    return false;
  }
  else if(lastName.value.match(letters) == null) {
    document.getElementById('messages').innerHTML = '<p class="error message">Invalid Last Name.</p>';
    lastName.style.border = "solid 2px #e61f1f";
    lastName.focus();
    return false;
  }
  else if(password1.value.length < 8) {
    document.getElementById('messages').innerHTML = '<p class="error message">Password too short. Must be at least 8 characters.</p>';
    password1.style.border = "solid 2px #e61f1f";
    password1.focus();
    return false;
  }
  else if(password1.value !== password2.value) {
    document.getElementById('messages').innerHTML = '<p class="error message">Passwords do not match.</p>';
    password2.style.border = "solid 2px #e61f1f";
    return false
  }
  else {
    return true;
  }
  }
