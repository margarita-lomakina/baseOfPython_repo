'use strict'

// es5

/*
function Product(name, price){
    this.name = name;
    this.price = price;
}

Product.prototype.make25PersonDiscount = function() {
    this.price = this.price * 0.75;
}
*/


// es6

class Product{
    constructor(name, price){
        this.name = name;
        this.price = price;
    }

    make25PersonDiscount(){
        this.price = this.price * 0.75;   
    }
}



let product1 = new Product('apple', 50);
product1.make25PersonDiscount();
console.log(product1.price);
