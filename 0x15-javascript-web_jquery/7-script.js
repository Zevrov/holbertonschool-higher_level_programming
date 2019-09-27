$.get('https://swapi.co/api/people/5/?format=json', function (corpus) {
  $('div#character').text(corpus.name);
});
