//                                                         // #Práctica lookups y views
// db = connect("mongodb://localhost/movies_practice");
// // Hacer una aggregated function que haga un lookup de la información de movies y directors.

// // Hacer una consulta donde se listen solo las peliculas hecha por
// // Christopher Nolan.
// db.directors.find({name: "Christopher Nolan"}).forEach(printjson)

// // Hacer una consulta donde se muestre la cantidad de péliculas de cada Director y los titulos de cada pélicula.
// db.createView("director_movie_count", "peliculas", [
//     {
//       $lookup: {
//         from: "directors",
//         localField: "director_id",
//         foreignField: "_id",
//         as: "director_info"
//       }
//     },
//     {
//       $unwind: "$director_info"
//     },
//     {
//       $group: {
//         _id: "$director_info.name",
//         number_of_movies: { $sum: 1 },
//         movies: { $push: "$title" }
//       }
//     }
//   ]);

// // Crear una vista por cada uno de los ejercicios anteriores.




db = connect("mongodb://localhost/movies_practice");
use.movies_practice

db.directors.insertMany([
  {
    _id: 1,
    name: "Christopher Nolan",
    birth_year: 1970,
    nationality: "British"
  },
  {
    _id: 2,
    name: "Quentin Tarantino",
    birth_year: 1963,
    nationality: "American"
  }
]);
db.movies.aggregate([
    {
      $lookup: {
        from: "directors",
        localField: "director_id",
        foreignField: "_id",
        as: "director_info"
      }
    },
    {
      $unwind: "$director_info"
    }
  ]);
// 2. Películas Hechas por Christopher Nolan
db.peliculas.aggregate([
    {
      $lookup: {
        from: "directors",
        localField: "director_id",
        foreignField: "_id",
        as: "director_info"
      }
    },
    {
      $unwind: "$director_info"
    },
    {
      $match: {
        "director_info.name": "Christopher Nolan"
      }
    }
  ]);
  // 3. Cantidad de Películas de Cada Director y Títulos de Cada Película
db.peliculas.aggregate([
    {
      $lookup: {
        from: "directors",
        localField: "director_id",
        foreignField: "_id",
        as: "director_info"
      }
    },
    {
      $unwind: "$director_info"
    },
    {
      $group: {
        _id: "$director_info.name",
        number_of_movies: { $sum: 1 },
        movies: { $push: "$title" }
      }
    }
  ]);
  // 4. Crear Vistas
// Vista para Lookup de Información de Movies y Directors
db.createView("movies_with_directors", "peliculas", [
    {
      $lookup: {
        from: "directors",
        localField: "director_id",
        foreignField: "_id",
        as: "director_info"
      }
    },
    {
      $unwind: "$director_info"
    }
  ]);
  // Vista para Películas Hechas por Christopher Nolan
  db.createView("nolan_movies", "peliculas", [
    {
      $lookup: {
        from: "directors",
        localField: "director_id",
        foreignField: "_id",
        as: "director_info"
      }
    },
    {
      $unwind: "$director_info"
    },
    {
      $match: {
        "director_info.name": "Christopher Nolan"
      }
    }
  ]);
  // Vista para Cantidad de Películas de Cada Director y Títulos
  db.createView("director_movie_count", "peliculas", [
    {
      $lookup: {
        from: "directors",
        localField: "director_id",
        foreignField: "_id",
        as: "director_info"
      }
    },
    {
      $unwind: "$director_info"
    },
    {
      $group: {
        _id: "$director_info.name",
        number_of_movies: { $sum: 1 },
        movies: { $push: "$title" }
      }
    }
  ]);