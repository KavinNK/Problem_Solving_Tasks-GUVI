var a = 10;

let random = function () {
    return Math.floor(Math.random() * 10)
}

function sum(x,y){
    return(a+random())

}

console.log(sum(a,random()))