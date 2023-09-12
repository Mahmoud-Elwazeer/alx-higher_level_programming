#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let input = c;
    if (input === undefined) {
      input = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let out = '';
      for (let j = 0; j < this.width; j++) {
        out += input;
      }
      console.log(out);
    }
  }
}

module.exports = Square;
