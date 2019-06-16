// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")

  } else {
    navbar.classList.remove("sticky");
  }
}

function openNavBar() {

    document.getElementById('sideNavBar').classList.remove('classname1')

      document.getElementById('sideNavBar').classList.add('classname');

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
  function main(){
    document.querySelector('.content').scrollIntoView({
      behavior: 'smooth'
    });

  }
