Mongosh
Mongod
copiar los el path y pegarlo en variables de entorno, instalar el link de el mongo https://www.mongodb.com/try/download/shell
copiar los datos de esa extraccion y pegarlos fuera de el /bin del disco local
help 
load("/direccion de el archivo donde quiere crearlo") para cargar el archivo
https://www.mongodb.com/docs/mongodb-shell/write-scripts/
db.movies.find()
db.movies.find().forEach(printjson);
db.movies.find({year:1997}).forEach(printjson);