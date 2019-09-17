#!/usr/bin/node

const process = require('process');
const arg = parseInt(process.argv[2]);
function factorial (arg) {
  if (x === 1 || isNaN(arg)) {
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
console.log(factorial(arg));
