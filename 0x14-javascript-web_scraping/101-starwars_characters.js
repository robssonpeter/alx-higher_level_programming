#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// console.log(url)
// fetch the movie
request.get(url, (error, response) => {
  if (!error) {
    const characters = JSON.parse(response.body).characters;
    for (let x = 0; x < characters.length; x++) {
      request.get(characters[x], (err, resp) => {
        if (!err) {
          const body = JSON.parse(resp.body);
          console.log(body.name);
        }
      });
    }
  } else {
    console.log(error);
  }
});
// get the characters
// loop through each character and get their name
