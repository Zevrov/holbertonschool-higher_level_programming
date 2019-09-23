#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    const arr = [];
    for (let index = 0; index < this.height; index++) {
      if (c === undefined) {
        arr.push('X');
      } else {
        arr.push(c);
      }
    }
    for (let index = 0; index < this.width; index++) {
      console.log(arr.join(''));
    }
  }
};
