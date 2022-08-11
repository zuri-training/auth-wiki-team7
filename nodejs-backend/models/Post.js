const mongoose = require("mongoose");

const postSchema = new mongoose.Schema({
    title: {
      type: String,
      required: true,
    },
    library_intro: {
      type: String,
    },
    library_content: {
      type: String,
    },
    author: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },
    likes: [
      {
        user: {
          type: mongoose.Schema.Types.ObjectId,
          ref: "User",
        },
      },
    ],
    image: String,
    preview: String,
  },
  { timestamps: true }
);

const Post = mongoose.model("Post", postSchema);
module.exports = Post;
