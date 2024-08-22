db = connect("mongodb://localhost/movies_practice");

db.movies.insertMany([
  {
    _id: 1,
    title: "Inception",
    year: 2010,
    director_id: 1,
    genres: ["Sci-Fi", "Action"],
    ratings: 8.8
  },
  {
    _id: 2,
    title: "Interstellar",
    year: 2014,
    director_id: 1,
    genres: ["Sci-Fi", "Drama"],
    ratings: 8.6
  },
  {
    _id: 3,
    title: "The Dark Knight",
    year: 2008,
    director_id: 1,
    genres: ["Action", "Crime"],
    ratings: 9.0
  },
  {
    _id: 4,
    title: "Pulp Fiction",
    year: 1994,
    director_id: 2,
    genres: ["Crime", "Drama"],
    ratings: 8.9
  }
]);

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