#!/usr/bin/node
from '101-data' import dict;
const new_dict = {};
const keys = Object.keys(dict);
const values = Object.values(dict);
for (let x = 0; x < keys.length; x++) {
  if (!new_dict[values[x]]) {
    new_dict[values[x]] = [keys[x]];
  } else {
    new_dict[values[x]].push(keys[x]);
  }
}
console.log(new_dict);
