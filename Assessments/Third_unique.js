const readline = require('readline');

const inp = readline.createInterface({
  input: process.stdin
});

const userInput = [];

inp.on("line", (data) => {
	userInput.push(data);
});

 

inp.on ("close", () => {
    
    var A=(userInput);
    var B = A[1].split(' ').map(Number);
    console.log(unique(B)) 
});

function unique(B){
    var count=0
    for (var i = 0; i < B.length; i++) {
            for (var j = 0; j < B.length; j++) 
                if (i != j && B[i] == B[j]) {
                    count=count+1;
                    break; 
                }
            if (count==3 && j == B.length) 
                return B[i]; 
        } 
}