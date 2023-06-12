#!/usr/bin/node
const args = process.argv.slice(2);
if (!args.length || isNaN(args[0])) {
  console.log('Missing size');
} else {
  let line;
  for (let x = 0; x < Number(args[0]); x++) {
    line = '';
    for (let y = 0; y < Number(args[0]); y++) {
      line += 'X';
    }
    console.log(line);
  }
}
