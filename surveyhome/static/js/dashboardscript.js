function openUserMenu(){
  user_menu = document.getElementsByClassName('user_menu');
  console.log("entered funtion")
  if(user_menu){
    console.log("user menu is present")
    for (var x=0; x < user_menu.length; x++){
      user_menu[x].style.visibility = 'visible';
      console.log("ieteration")
    }
  }
}
