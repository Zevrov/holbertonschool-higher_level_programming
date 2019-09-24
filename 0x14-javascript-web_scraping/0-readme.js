#!/usr/bin/node

const readme = require('fs');
readme.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
