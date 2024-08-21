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

    db = connect('mongodb://localhost/movies');
    db.moviesList.find().forEach(printjson);
    db.moviesList.find({year: 1997}).forEach(printjson);
    db.moviesList.find({year: {$eq: 1997}}).forEach(printjson);//equal
    
    list = db.moviesList.find({}, {title:1, _id:0});
    console.log(list);
    db.moviesList.find({year: 1997}, {title:1, _id:0}).forEach(printjson);
    
    db.moviesList.updateOne({title: "Casablanca"},
      {
        $set: {
          year: 1942,
          directtion: "Michael Curtiz"
        }
      }
    )
    
    db.moviesList.updateMany({dummy_data: "hello"},
      {
        $set: {
          dummy_data: "world"
        }
      }
    )
    
    db.moviesList.updateOne({dummy_data: "world"},
      {
        $set: {
          dummy_data: "hello"
        }
      }
    )
    
    db.moviesList.deleteOne({title: "Casablanca"});
    db.moviesList.deleteMany({title: "Titanic"});
    
    db.moviesList.find({genres: "Drama"}).forEach(printjson);
    db.moviesList.find({genres: {$in:["Drama","Animation"]}}).forEach(printjson);
    db.moviesList.find({genres: {$all:["Drama","Romance"]}}).forEach(printjson);
    
    db.moviesList.find({$or: [{year: 1997}, {year: 2001}]}).forEach(printjson);
    db.moviesList.find({$and: [{genres: "Animation"}, {year: 2001}]}).forEach(printjson);
    db.moviesList.find({$nor: [{genres: "Animation"}, {genres: "War"}]}).forEach(printjson);//not or
    db.moviesList.find({genres: {$not: {$in: ["Animation", "War"]}}}).forEach(printjson);//lo mismo que el de abajo
    db.moviesList.find({genres: {$nin: ["Animation", "War"]}}).forEach(printjson);//lo mismo que el de arriba pero con $nin
    db.moviesList.find({year: {$ne: 2001}}).forEach(printjson);//not equal
    db.moviesList.find({year: {$gt: 1997}}).forEach(printjson);//greater than
    db.moviesList.find({year: {$gte: 1997}}).forEach(printjson);//greater than or equal
    db.moviesList.find({year: {$lt: 1997}}).forEach(printjson);//less than
    db.moviesList.find({year: {$lte: 1997}}).forEach(printjson);//less than or equal
    db.moviesList.find({title: {$regex: "^S"}}).forEach(printjson);//starts with S
    db.moviesList.find({title: {$not: {$regex: "^S"}}}).forEach(printjson);//Doesn't starts with S
    db.moviesList.find().sort({year: 1}).forEach(printjson);//sort ascending
    db.moviesList.find().sort({year: -1}).forEach(printjson);//sort descending
    db.moviesList.find().limit(2).forEach(printjson);//limit results
    db.moviesList.find().skip(2).forEach(printjson);//skip first 2 results
    