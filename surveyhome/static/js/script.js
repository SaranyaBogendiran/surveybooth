window.onscroll = function() {myFunction()};
var mediaquery = window.matchMedia('(max-width: 1024px)');
var closeNavBarVar = document.getElementById('sideNavBarCloseSVG');
var toogle_lineSVG = document.getElementById('toogle_line');
if (mediaquery.matches){
      toogle_lineSVG.setAttribute("viewBox", "0 0 60 120");
      document.getElementById('toogle_link_path').setAttribute("d","M0,5 100,5 M0,35 100,35 M0,70 100,70")
}

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

//Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

// open user name

function openUserMenu(){
  document.getElementById('user_menu').style.visibility = 'visible';

}

function openNavBar() {

    document.getElementById('sideNavBar').classList.remove('classname1')

    document.getElementById('sideNavBar').classList.add('classname');
    if (mediaquery.matches){
           closeNavBarVar.setAttribute("viewBox", "0 0 75 75");
     }

}

function closeNavBar() {
 // document.getElementById('sideNavBarList').style.display='none';
document.getElementById('sideNavBar').classList.remove('classname');
document.getElementById('sideNavBar').classList.add('classname1');

}
function signup(){
  document.querySelector('.signup').scrollIntoView({
    behavior: 'smooth'
  });
}
  function signin(){
    document.querySelector('.signin').scrollIntoView({
      behavior: 'smooth'
    });

  }
  function contact(){
    document.querySelector('.contactpg').scrollIntoView({
      behavior: 'smooth'
    });
}
