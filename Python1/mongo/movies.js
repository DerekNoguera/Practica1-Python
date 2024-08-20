db = connect( 'mongodb://localhost/movies' );
db.movies.insertMany( [
    {
       title: 'Titanic',
       year: 1997,
       genres: [ 'Drama', 'Romance' ]
    },
    {
       title: 'Spirited Away',
       genres: 2001,
       genres: [ 'Animation', 'Adventure', 'Family' ]
    },
    {
       title: 'Casablanca',
       genres: [ 'Drama', 'Romance', 'War' ]
    }
 ] )