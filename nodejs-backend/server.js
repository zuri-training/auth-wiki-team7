var express = require("express");
const path = require("path");
var app = express();

// set the view engine to ejs
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));
// use res.render to load up an ejs view file
let pets = [
  {
    name: "Meowsalot",
    description: "From the tiny Rusty-spotted cat of Sri Lanka to the massive Siberian tiger of the Russian Far East, there are 40 species of wild cats in the world, and each of them is as beautiful as it is unique.Most of us know lions, tigers, jaguars and leopards, but what are all the other types of wild cats out there? If you consider yourself a cat person or simply curious about these charismatic animals, read on to meet the family. They are the most loved and cute species found on the land.",
    species: "cat",
    image: "https://540934-1733880-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2020/05/Eurasian-lynx-AdobeStock_246336076-1024x683.jpg",
  },
  {
    name: "Barksalot",
    description: "Dogs are the most variable mammal on earth with around 450 globally recognized dog breeds.[10] In the Victorian era, directed human selection developed the modern dog breeds, which resulted in a vast range of phenotypes. Most breeds were derived from small numbers of founders within the last 200 years, and since then dogs have undergone rapid phenotypic change and were formed into today's modern breeds due to artificial selection imposed by humans.",
    species: "dog",
    image: "https://upload.wikimedia.org/wikipedia/commons/e/e0/Dog_niemiecki_%C5%BC%C3%B3%C5%82ty_LM980.jpg",
  }
];
// index pages
let dir = "";
app.get("/", function (req, res) {
  res.render("pages/index");
});

// about page
app.get("/about", function (req, res) {
  res.render("pages/about", {pets});
});
// login page
app.get("/login", function (req, res) {
  res.render("pages/login",);
});


app.listen(8080);
console.clear();
console.log("Server is listening on port 8080");
