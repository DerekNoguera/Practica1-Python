db = connect('mongodb://localhost/libros')
use.libros
db.libros.insertMany([

    { "titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "genero": "Ficción", "año": 1925 },
    
    { "titulo": "Matar a un Ruiseñor", "autor": "Harper Lee", "genero": "Ficción", "año": 1960 },
    
    { "titulo": "1984", "autor": "George Orwell", "genero": "Ciencia Ficción", "año": 1949 },
    
    { "titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "genero": "Romance", "año": 1813 },
    
    { "titulo": "El Guardián entre el Centeno", "autor": "J.D. Salinger", "genero": "Ficción", "año": 1951 }
    
])
db.libros.find().forEach(printjson)

// Cambie / Actualice el género del libro llamado “1984” a que sea “Drama”
db.libros.updateOne({titulo: "1984"},
    {
        $set: {genero: "Drama"}
    }
)
// Elimine el documento de la colección "libros" donde el nombre del autor sea “J.D. Salinger”
db.libros.deleteOne({autor: "J.D. Salinger"})

                                        // Práctica - Filtrado

// Liste el titulo de los libros que fueron publicados luego de 1940
db.libros.find({año:{$gt: 1940}}).forEach(printjson)

// Busque los libros que pertenezcan a un género específico. Elija un género y muestre los
// títulos y autores de los libros en ese género.
db.libros.find({genero: "Ficción"}).forEach(printjson)

// Encuentre todos los libros escritos por un autor específico. Elija un autor y muestre los
// títulos y géneros de los libros escritos por ese autor.
db.libros.find({autor: "Jane Austen"}).forEach(printjson)

// Liste únicamente los 2 primeros libros que fueron publicados luego de 1900 y ordenelos por
// titulo de manera descendente
db.libros.find({año:{$gt: 1900}}).limit(2).forEach(printjson)

// Busque todos los libros. Una vez realizado esto y revisando cuáles son los valores que se
// retornaron, retorne únicamente los 2 últimos libros del resultado anterior
db.libros.find().sort({año: -1}).limit(2).forEach(printjson)

                                        // Práctica - Agregación

// Calcule el número total de libros en la colección "libros".
db.libros.count()

// Agrupe los libros en la colección "libros" por año y muestra la cantidad de libros publicados
// cada año.
db.libros.aggregate(
    {
    $group: {_id: "$año", count: {$sum: 1}}
})

// Calcule el año promedio de publicación para los libros.
db.libros.aggregate([
  {
    $group: {
      _id: null,
      promedioAnio: { $avg: "$año" }
    }
  }
]).forEach(printjson);

// Obtenga la lista de géneros únicos presentes en la colección "libros" y muestra los géneros
// en orden alfabético.
db.libros.distinct("titulo").sort().forEach(printjson);





                            // Práctica - Agregación

// Describa lo que hace el siguiente código
db.libros.aggregate([
    {
        $group:{
            _id: "$genero",
            totalDeLibros: {$sum: 1},
            anioPromedioDePublicacion:{$avg: "$año"}
        }
    },
    {$sort: {totalSales: -1}},
    {$limit: 5}
])
//            R/
// Hace un grupo donde muestra el genero que mas se repite,muestra la catidad que se repite ese genero
// Y saca el promedio de todos los años existentes, hace un sorted de el numero de ventas para que lo muestre decreciente
//usando el totalSales de abajo y hace que sea un limite de 5

                            // Práctica - Agregación

// Describa lo que hace el siguiente código
db.sales.aggregate([
    {
        $match:{
            date: {$gte: ISODate("2022-01-01"), $lte: ISODate("2022-12-31")}
        }
    },
    {
        $group:{
            _id: "$product",
            totalSales:{ $sum: "$quantity"},
            averagePrice:{$avg: "$price"}
        }
    },
    {$sort:{totalSales: -1}},
    {$limit: 5}
])
// Se conecta a la carpeta sales, elegimos elementos que queremos agarrar en el $match, luego hacemos un grupo en el que se muestra el id de el producto, la cantidad de ventas
// y el promedio de el precio, abajo se crea un sort y ese totalSales es el que se le envia a el aggregate de arriba donde tambien se le hace un sort()
// y se hace un limite de 5 tambien