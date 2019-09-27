$.get('https://swapi.co/api/films/?format=json', function (corpus) {
  for (const movie of corpus.results) {
  $('ul#list_movies').append('<li>' + movie.title + '</li>');
}
