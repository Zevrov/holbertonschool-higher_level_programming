#!/usr/bin/node
module.exports = class Rectangle {
  constructor (x, y) {
    if (x > 0 && y > 0) {
      this.width = x;
      this.height = y;
    }
  }

  print () {
    const array = [];
    for (let index = 0; index < this.width; index++) {
      array.push('X');
    }
    for (let index = 0; index < this.height; index++) {
      console.log(array.join(''));
    }
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
