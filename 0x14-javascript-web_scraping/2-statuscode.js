#!/usr/bin/node

const status = require('request');
status(process.argv[2], (error, response) => {
  if (error) {}
  console.log('code:', response.statusCode);
});
