//Question: Find the datatype of author age in Nodejs Object.

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

console.log(typeof(library[1].authorDetails.age))