"use strict";

alert("Задание 4");

const products = [
        {
            id: 3,
            price: 127,
            photos: [
                "1.jpg",
                "2.jpg"
            ]
        },
        {
            id: 5,
            price: 499,
            photos: []
        },
        {
            id: 10,
            price: 26,
            photos: [
                "3.jpg"
                ]
        },
        {
            id: 8,
            price: 78
        }
    ];

let sort_products = products.slice();
const result = products.filter(product => "photos" in product && product.photos.length > 0);
console.log(result);

function compare(a, b) {
    if (a.price < b.price) {
      return -1;
    }
    if (a.price > b.price) {
      return 1;
    }
    return 0;
  }

sort_products.sort(compare);
console.log(sort_products);

