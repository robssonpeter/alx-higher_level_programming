#!/usr/bin/node
const args = process.argv.slice(2);
let max = 0;
let secondMax = 0;
for (let x = 0; x < args.length; x++) {
  if (Number(args[x]) > max) {
    max = Number(args[x]);
  }
}

for (let x = 0; x < args.length; x++) {
  if (Number((args[x]) > secondMax && Number(args[x]) < max)) {
    secondMax = Number(args[x]);
  }
}
console.log(secondMax);
