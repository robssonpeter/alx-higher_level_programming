#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (!error) {
    const results = JSON.parse(response.body);
    const output = {};
    for (let x = 0; x < results.length; x++) {
      if (results[x].completed) {
        if (!output[results[x].userId]) {
          output[results[x].userId] = 1;
        } else {
          output[results[x].userId] += 1;
        }
      }
    }
    console.log(output);
  }
});
