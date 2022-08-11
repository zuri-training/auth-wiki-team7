const User = require('../models/User')
const bcrypt = require('bcrypt')
// const router = require('express').Router()

const createUser = async (req,res) => {
    User?.exists({ email: req.body.email })
      .then(async (result) => {
        if (!result) {
          try {
            const salt = await bcrypt.genSalt(10);
            const hashedPassword = await bcrypt.hash(req.body.password, salt);
            const user = new User({
                ...req.body, password: hashedPassword
              });
              await user
                .save()
                .then((result) => {
                  return res.status(201).send(result);
                })
                .catch((err) => {
                  return res.status(501).send(err);
                });
          } catch (error) {
            console.log(error);
          }
        } else {
          res.status(409).json({
            message: "User already Exist",
          });
        }
      })
      .catch((err) => console.error(err));
}


module.exports = {createUser}