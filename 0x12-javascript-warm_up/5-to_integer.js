#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(args[0]));
}
