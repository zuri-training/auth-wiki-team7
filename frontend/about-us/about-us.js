let menuBtn = document.querySelector(".menu_btn");
let navCard = document.querySelector(".nav_card");

menuBtn.addEventListener("click", () => {
    navCard.classList.toggle("hide");
})