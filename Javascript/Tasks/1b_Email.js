//Question : Insert a new key called email and assign a value email1@gmail.com and email2@gmail.com respectively in both authorDetails object;

var library = [
    {
    title : "Javascript",
    price : 500,
    readers : [
        {
            name : "Person 1",
            count : 300
        },  
        {
            name : "Person 2",
            count : 400
        }
    ],
    authorDetails : {
        name : "Raj",
        age : 40
    }
    },
    {
    title : "Nodejs",
    price : 600,
    readers : [],
    authorDetails : {
        name : "Raj",
        age : 40
    }
    }
]

//Answer:

library[0].email = 'email1@gmail.com'
library[1].email = 'email2@gmail.com'

console.log(library)

