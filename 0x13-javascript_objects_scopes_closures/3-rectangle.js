#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let out = '';
      for (let j = 0; j < this.width; j++) {
        out += 'X';
      }
      console.log(out);
    }
  }
}

module.exports = Rectangle;
