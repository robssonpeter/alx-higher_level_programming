#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg[0]) {
  console.log(arg[0]);
} else {
  console.log('No argument');
}
