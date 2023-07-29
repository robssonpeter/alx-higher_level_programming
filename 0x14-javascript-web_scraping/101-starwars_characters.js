#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response) => {
  if (!error) {
    const characters = JSON.parse(response.body).characters;
    const charIds = [];
    characters.sort();
    let currentChar = [];
    for (let x = 0; x < characters.length; x++) {
      currentChar = characters[x].split('/');
      charIds.push(Number(currentChar[currentChar.length - 2]));
    }
    charIds.sort((a, b) => a - b);
    const url = 'https://swapi-api.alx-tools.com/api/people/';
    const output = {};
    for (let x = 0; x < charIds.length; x++) {
      request.get(url + charIds[x], (err, resp) => {
        if (!err) {
          const body = JSON.parse(resp.body);
          output[x] = body.name;
        }
      });
    }
    setTimeout(() => {
      for (let x = 0; x < charIds.length; x++) {
        console.log(output[x]);
      }
    }, 5000);
  } else {
    console.log(error);
  }
});
