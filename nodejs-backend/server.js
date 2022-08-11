const express = require("express");
const mongoose = require("mongoose");
require('dotenv').config()
const path = require("path");
const app = express();

// set the view engine to ejs
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

// Are we in production or development?
const isProduction = process.env.NODE_ENV === "production";
console.info(`Environment isProduction = ${isProduction}`);

// Connect to NoSQL datastore........................

// choose the connection
const dbURI = isProduction
  ? encodeURI(process.env.MONGO_DB_ATLAS)
  : encodeURI(process.env.LOCAL_MONGODB_URI);
console.info("MongoDB URL = " + dbURI);

// get dbName
const DB_NAME = process.env.DB_NAME;

// set connection options
const connectionOptions = {
  useNewUrlParser: true,
  useUnifiedTopology: true,
};

// use mongoose to connect & create a default connection
mongoose.connect(dbURI, connectionOptions, (err, client) => {
  if (err) {
    console.error(
      "Error in MongoDB connection : " + JSON.stringify(err, undefined, 2)
    );
    return
  }
  console.info("MongoDB connection succeeded.");
});

// Get the default connection
const connection = mongoose.connection;

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
  res.render("pages/login");
});
// signup page
app.get("/signup", function (req, res) {
  res.render("pages/signup");
});
// product page
app.get("/products", function (req, res) {
  res.render("pages/product");
});
// documentation page
app.get("/documentation", function (req, res) {
  res.render("pages/documentation");
});
// Error page
app.get("*", function (req, res) {
  res.render("pages/error");
});

app.listen(process.env.PORT || 4000);
// console.clear();
console.log("Server is listening on port:", process.env.PORT || 4000);
