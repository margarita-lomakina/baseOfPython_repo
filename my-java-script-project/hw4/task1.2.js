'use strict'
// es5

/*
function Post(author, text, date){
    this.author = author;
    this.text = text;
    this.date = date;
}

Post.prototype.edit = function(text){
    this.text = text;
}

function AttachedPost(author, text, date){
    Post.call(this, author, text, date);
    this.highlighted = false;
}

AttachedPost.prototype = Object.create(Post.prototype);
AttachedPost.prototype.constructor = AttachedPost;

AttachedPost.prototype.makeTextHighlighted = function(){
    this.highlighted = true;
}
*/


// es6
class Post{
    constructor(author, text, date){
        this.author = author;
        this.text = text;
        this.date = date;
    }

    edit(text){
        this.text = text;   
    }
}

class AttachedPost extends Post{
    constructor(author, text, date){
        super(author, text, date);
        this. highlighted = false;
    }

    makeTextHighlighted(){
        this.highlighted = true;
    }
}


let post1 = new Post("John", "hello world", "27.08.2021");
let attachedPost1 = new AttachedPost("Kate", "All you need love", "28.08.2021");
post1.edit("Hello, World!");
attachedPost1.edit("All you need is love");
attachedPost1.makeTextHighlighted();
console.log(post1);
console.log(attachedPost1);
