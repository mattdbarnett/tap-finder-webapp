function validateSignupForm() {
  var firstName = document.getElementById("FirstName");
  var lastName = document.getElementById("LastName");

  var letters = /^[A-Za-z]+$/;
  if(firstName.value.match(letters) == null) {
    document.getElementById('main-content').innerHTML = '<p class="error">First Name Cannot Contain Numbers!</p>';
    firstName.focus();
    return false;
  }
  else if(lastName.value.match(letters) == null) {
    alert('Error Submitting Form: Last Name Cannot Contain Numbers!');
    lastName.focus();
    return false;
  }
  else {
    return true;
  }
  }
