#!/usr/bin/node
const file = require('fs');
const path = process.argv[2];
file.writeFile(path, process.argv[3], (error) => {
  if (error) {
    console.log(error);
  }
});
