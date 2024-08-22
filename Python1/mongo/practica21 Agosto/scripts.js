db = connect("mongodb://localhost/libreria_practica");

/* db.libros.insertMany([
  {
    titulo: "El Gran Gatsby",
    autor: "F. Scott Fitzgerald",
    genero: "Ficción",
    año: 1925,
  },
  {
    titulo: "Matar a un Ruiseñor",
    autor: "Harper Lee",
    genero: "Ficción",
    año: 1960,
  },
  {
    titulo: "1984",
    autor: "George Orwell",
    genero: "Ciencia Ficción",
    año: 1949,
  },
  {
    titulo: "Orgullo y Prejuicio",
    autor: "Jane Austen",
    genero: "Romance",
    año: 1813,
  },
  {
    titulo: "El Guardián entre el Centeno",
    autor: "J.D. Salinger",
    genero: "Ficción",
    año: 1951,
  },
]); */

/* db.libros.insertMany(
  [
    {
      titulo: "Crónica de una muerte anunciada",
      autor: "Gabriel García Márquez",
      genero: "Ficción",
      año: 1981,
    },
    {
      titulo: "Cien años de soledad",
      autor: "Gabriel García Márquez",
      genero: "Ficción",
      año: 1967,
    },
    {
      titulo: "La casa de los espíritus",
      autor: "Isabel Allende",
      genero: "Ficción",
      año: 1982,
    },
  ]
); */

/* db.libros.find({}, { _id: 0, titulo: 1, autor: 1 }).forEach(printjson);
db.libros.updateOne({ titulo: "1984" }, { $set: { genero: "Drama" } });
db.libros.deleteMany({ autor: "J.D. Salinger" });*/

/* db.libros.find({año: { $gt: 1940}}).forEach(printjson);
db.libros.find({genero: "Ficción"}, {_id: 0, titulo: 1, autor: 1}).forEach(printjson);
db.libros.find({autor: "Isabel Allende"}, {_id: 0, titulo: 1, genero: 1}).forEach(printjson);
db.libros.find({año: { $gt: 1900 }}).sort({año: -1}).limit(2).forEach(printjson);*/

/* lista = db.libros.find().toArray();
console.log("Lista de libros:");
printjson(lista);
console.log("Últimos dos libros:");
printjson(lista.at(-2));
printjson(lista.at(-1));*/

/* db.libros.aggregate([
  {
    $count: "Cantidad de libros:"
  }
]).forEach(printjson); */

/* db.libros.aggregate([
  {
    $group: {
      _id: "$genero",
      total: { $sum: 1 }
    }
  }
]).forEach(printjson); */

/* db.libros.aggregate([
  {
    $group: {
      _id: null,
      avg: { $avg: "$año" }
    }
  },
  {
    $project: {
      _id: 0,
      promedio: "$avg",
      promedioRedondeado: { $round : ["$avg", 0] }
    }
  }
]).forEach(printjson); */

db.libros.aggregate([
  {
    $group: {
      _id: { genero: "$genero", autor: "$autor" },
    }
  },
  {
    $sort: { "_id.autor": -1, "_id.genero": 1 }
  }
]).forEach(printjson);