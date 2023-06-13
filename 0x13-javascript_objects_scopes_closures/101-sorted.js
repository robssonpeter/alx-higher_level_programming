#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
const keys = Object.keys(dict);
const values = Object.values(dict);
for (let x = 0; x < keys.length; x++) {
  if (!newDict[values[x]]) {
    newDict[values[x]] = [keys[x]];
  } else {
    newDict[values[x]].push(keys[x]);
  }
}
console.log(newDict);
