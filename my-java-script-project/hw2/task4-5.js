"use strict";

alert("Задание 4");

function add(a, b){
    return a + b;
}
function sub(a, b){
    return a-b;
}
function division(a, b){
    return a/b;
}
function mult(a, b){
    return a*b;
}

let number1 = 8, number2 = 5;
alert(add(number1, number2));
alert(sub(number1, number2));
alert(division(number1, number2));
alert(mult(number1, number2));

alert("Задание 5");

function mathOperation(arg1, arg2, operation){
    switch(operation){
        case "+":
            return add(arg1, arg2);
        case "-":
            return sub(arg1, arg2);
        case "*":
            return mult(arg1, arg2);
        case "/":
            return division(arg1, arg2);
        default:
            return "Нет такой операции";
    }       
}

alert(mathOperation(18, -5, "+"));