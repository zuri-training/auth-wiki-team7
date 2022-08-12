
let menuBtn = document.querySelector(".menu_btn");
let navCard = document.querySelector(".nav_card");

let none = document.getElementById("none")
let no = document.getElementById("no")
let close_no = document.getElementById("close-no")
let copy_code = document.getElementById("copy_code")

menuBtn.addEventListener("click", () => {
    navCard.classList.toggle("hide");
})

if(close_no){
  close_no.addEventListener("click", function(){
    no.style.display = "none"
  })
}

const copyButtonLabel = "Copy Code";

// you can use a class selector instead if you, or the syntax highlighting library adds one to the 'pre'. 
let blocks = document.querySelectorAll("pre");

blocks.forEach((block) => {
  // only add button if browser supports Clipboard API
  if (navigator.clipboard) {
    let button = document.createElement("button");
    button.innerText = copyButtonLabel;
    button.addEventListener("click", copyCode);
   
    block.appendChild(button);
  }
});

async function copyCode(event) {
  if(none){
    no.style.display = "grid"
    return
  }
  const button = event.srcElement;
  const pre = button.parentElement;
  let code = pre.querySelector("code");
  let text = code.innerText;
  await navigator.clipboard.writeText(text);
  
  button.innerText = "Code Copied";
  setTimeout(()=> {
    button.innerText = copyButtonLabel;
  },1000)
}
  


  






