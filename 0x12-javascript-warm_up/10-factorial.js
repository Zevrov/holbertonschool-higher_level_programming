#!/usr/bin/node

const process = require('process');
const arg = parseInt(process.argv[2]);
function factorial (arg) {
<<<<<<< HEAD
  if (arg === 1 || isNaN(arg)) {
=======
  if (x === 1 || isNaN(arg)) {
>>>>>>> 8f85dce0a56c9dab68ba3c89959a068e319bf5ed
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
console.log(factorial(arg));
