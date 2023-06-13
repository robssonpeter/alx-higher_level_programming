#!/usr/bin/node
const OldSquare = require('./5-square');
module.exports = class Square extends OldSquare {
  constructor (size) {
    super();
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    for (let h = 0; h < this.height; h++) {
      let line = '';
      for (let w = 0; w < this.width; w++) {
        if (c) {
          line += c;
        } else {
          line += 'X';
        }
      }
      console.log(line);
    }
  }
};
