const mongoose = require('mongoose')

const commentSchema = new mongoose.Schema({
    post: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Post",
        required: true
      },
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Post",
        required: true
      },
    content: {
        type: String,
        required: true
    },
}, {timestamps:true})

const Comment = mongoose.model("Comment", commentSchema);
module.exports = Comment;