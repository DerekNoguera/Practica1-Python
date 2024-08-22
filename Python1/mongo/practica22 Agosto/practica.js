                                                        // #Práctica lookups y views
db = connect("mongodb://localhost/movies_practice");
// Hacer una aggregated function que haga un lookup de la información de movies y directors.

// Hacer una consulta donde se listen solo las peliculas hecha por
// Christopher Nolan.
db.directors.find({name: "Christopher Nolan"}).forEach(printjson)
// Hacer una consulta donde se muestre la cantidad de péliculas de cada Director y los titulos de cada pélicula.

// Crear una vista por cada uno de los ejercicios anteriores.