function tapValidate() {

  if( document.tapForm.emailAddress.value == "" ) {
    alert( "Please enter your email address." );
    document.tapForm.emailAddress.focus() ;
    return false;
  }

  if( document.tapForm.lat.value == "" ) {
    alert( "Please enter the latitude of your tap." );
    document.tapForm.lat.focus() ;
    return false;
  }

  if( document.tapForm.long.value == "" ) {
    alert( "Please enter the longitude of your tap." );
    document.tapForm.long.focus() ;
    return false;
  }

  return tapSubmit()

}

function tapSubmit() {

}
