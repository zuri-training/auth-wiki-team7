var express = require("express");
const path = require("path");
var app = express();

// set the view engine to ejs
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

// index pages
let dir = "";
app.get("/", function (req, res) {
  res.render("pages/index");
});

// about page
app.get("/about", function (req, res) {
  res.render("pages/about");
});
// login page
app.get("/login", function (req, res) {
  res.render("pages/login",);
});
// signup page
app.get("/signup", function (req, res) {
  res.render("pages/signup",);
});
// product page
app.get("/products", function (req, res) {
  res.render("pages/product",);
});
// documentation page
app.get("/documentation", function (req, res) {
  res.render("pages/documentation",);
});
// Error page
app.get("*", function (req, res) {
  res.render("pages/error",);
});

app.listen(8080);
console.clear();
console.log("Server is listening on port 8080");
