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


var divToHide = document.getElementById('user_menu');
document.onclick = function(e){
    console.log("asdas")
    if(e.target.id !== 'user_menu'){
      //element clicked wasn't the div; hide the div
      for (var x=0; x < divToHide.length; x++){
        divToHide[x].style.visibility = 'visible';
        console.log("ieteration")
      }
    }
};
