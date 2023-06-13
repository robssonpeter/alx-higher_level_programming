#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const h = this.width;
    const w = this.height;
    this.width = w;
    this.height = h;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
