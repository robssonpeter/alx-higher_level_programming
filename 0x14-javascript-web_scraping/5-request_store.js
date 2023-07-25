#!/usr/bin/node
const request = require('request');
const file = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  file.writeFile(fileName, response.body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
