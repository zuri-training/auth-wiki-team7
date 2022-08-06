let eye_open = document.getElementById("eye_open")
let eye_close = document.getElementById("eye_close")
let password = document.getElementById("password")
let eye_open2 = document.getElementById("eye_open2")
let eye_close2 = document.getElementById("eye_close2")
let password2 = document.getElementById("password2")

//first password
eye_open.addEventListener("click", function(e){
    eye_close.classList.add("show")
    eye_close.style.display = "block"
    eye_open.style.display = "none"
    password.type = "text"
})
eye_close.addEventListener("click", function(e){
    eye_close.style.display = "none"
    eye_open.style.display = "block"
    password.type = "password"
})

// second password
eye_open2.addEventListener("click", function(e){
    eye_close2.classList.add("show")
    eye_close2.style.display = "block"
    eye_open2.style.display = "none"
    password2.type = "text"
})

eye_close2.addEventListener("click", function(e){
    eye_close2.style.display = "none"
    eye_open2.style.display = "block"
    password2.type = "password"
})