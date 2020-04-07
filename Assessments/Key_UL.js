const readline = require('readline');

const inp = readline.createInterface({
  input: process.stdin
});

const userInput = [];

inp.on("line", (data) => {
	userInput.push(data);
});

inp.on("close", () => {
	var A=(userInput);
	var B=A[0].split('').map(String)
	var C=parseInt(A[1])
	var Key=parseInt(A[2])
	var myfunc = myfun(B,C,Key)
	let ans = '';
	for(i=0;i<myfunc.length;i++){
      ans += myfunc[i]
    }
	console.log(ans)
});

function myfun(B,C,Key){
    if(C==1)
    {
        for(i=0;i<B.length;i++){
            if((i+1)%Key==0)
            B[i]=B[i].toLowerCase()
        }
        return B
    }
    else  if(C==2)
    {
        for(i=0;i<B.length;i++){
            if((i+1)%Key==0)
            B[i]=B[i].toUpperCase()
        }
        return B
    }
}