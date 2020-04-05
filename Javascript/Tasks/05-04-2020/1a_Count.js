//Question: Update the count of Person 2 inside readers Array in Javascript;

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

library[0].readers[1].count = 800
console.log(library[0].readers[1].count)