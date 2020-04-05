//Question: Create a New Object in the library for a new Book called SQL.

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

library[2] = {
    title : "SQL",
    price : 500,
    readers : [
        {
            name : "Person 1",
            count : 300
        }
    ],
    authorDetails : {
        name : "Raj",
        age : 40
    }
}

console.log(library[2])

