#!/usr/bin/node
const file = require('fs');
const path = process.argv[2];
file.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
