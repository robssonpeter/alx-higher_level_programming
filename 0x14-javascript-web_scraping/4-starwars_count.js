#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (error, response) => {
  const data = JSON.parse(response.body);
  const filtered = data.results.filter((elements) => {
    return elements.characters.indexOf(characterUrl) > -1;
  });
  if (!error) {
    console.log(filtered.length);
  }
});
