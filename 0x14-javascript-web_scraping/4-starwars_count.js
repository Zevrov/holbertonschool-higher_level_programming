#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) { return; }
  let count = 0;
  const result = JSON.parse(body).results;
  for (const movie of result) {
    for (const character of movie.characters) {
      if (character.includes('/18/') || character.includes('/18')) {
        count++;
      }
    }
  }
  console.log(count);
});
