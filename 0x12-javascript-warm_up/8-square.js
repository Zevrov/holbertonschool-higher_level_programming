#!/usr/bin/node

const process = require('process');
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < arg; index++) {
    console.log('X'.repeat(arg));
  }
}
