#!/usr/bin/node

const readme = require('fs');
readme.readFile(process.argv[2], 'utf-8', (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(response);
  }
});
