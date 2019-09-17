#!/usr/bin/node

const process = require('process');
const arg = process.argv[2];
const String = 'C is fun';
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < arg; index++) {
    console.log(String);
  }
}
