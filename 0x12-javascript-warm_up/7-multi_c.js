#!/usr/bin/node
const args = process.argv.slice(2);
if (!args.length) {
  console.log('Missing number of occurrences');
} else if (!isNaN(args[0])) {
  for (let x = 0; x < Number(args[0]); x++) {
    console.log('C is fun');
  }
}
