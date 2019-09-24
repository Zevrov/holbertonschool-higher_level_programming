#!/usr/bin/node

const writeme = require('fs');
writeme.writeFile(process.argv[2], process.argv[3], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
