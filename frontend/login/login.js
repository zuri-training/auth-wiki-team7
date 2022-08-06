let eye_open = document.getElementById("eye_open")
let eye_close = document.getElementById("eye_close")
let password = document.getElementById("password")
let illustration = document.getElementById("illustration")

eye_open.addEventListener("click", function(e){
    eye_close.classList.add("show")
    eye_close.style.display = "block"
    eye_open.style.display = "none"
    password.type = "text"
    // eye_open.classList.remove("show")
})

eye_close.addEventListener("click", function(e){
    // eye_open.classList.add("show")
    eye_close.style.display = "none"
    eye_open.style.display = "block"
    password.type = "password"
    // eye_close.classList.remove("show")
})

function detectBrowser() {
    if (navigator.userAgent.includes("Chrome")) {
      return "chrome"
    }
    if (navigator.userAgent.includes("Firefox")) {
      return "firefox"
    }
    if (navigator.userAgent.includes("Safari")) {
      return "safari"
    }
  }
  illustration.classList.add(detectBrowser())