db = connect('mongodb://localhost/movies');
// db.movies.find({year:1997}).forEach(printjson);
// db.movies.updateOne({title:"Casablanca"}),
//     {
//         $set: {year:1998}
//     }

db.movies.updateOne({dummy_data: "Hola  "}, 
    {
        $set:{
            dummy_data: "World"
        }
    })
    