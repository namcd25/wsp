
function openNav() {
  document.getElementById("mySidenav").style.width = "50%";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

let sizeButton = document.getElementsByClassName('size_btn')
sizeButton.addEventListener('click', function(e) {
  if (e.target && e.target.nodeName === "a") {
    let elements = document.getElementById('main-li').children;
    for (let i = 0; i < elements.length; ++i) {
        elements[i].classList.remove("active");
    }
    e.target.classList.add("active-class");
 }
});

function displaySelectedShoeDetails() {
  const shoeSelect = document.getElementById("shoeName");
  const selectedShoe = shoeSelect.options[shoeSelect.selectedIndex].text;

  const sizeSelect = document.getElementById("shoeSize");
  const selectedSize = sizeSelect.options[sizeSelect.selectedIndex].text;

  console.log("Nama Sepatu: " + selectedShoe);
  console.log("Ukuran Sepatu: " + selectedSize);
}

window.onload = function() {
  const shoeSelect = document.getElementById("shoeName");
  shoeSelect.addEventListener("change", displaySelectedShoeDetails);

  const sizeSelect = document.getElementById("shoeSize");
  sizeSelect.addEventListener("change", displaySelectedShoeDetails);
};
