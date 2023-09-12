#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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

module.exports = square;
