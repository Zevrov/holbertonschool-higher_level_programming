$(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (corpus) {
    $('div#hello').text(corpus.hello);
  });
});
