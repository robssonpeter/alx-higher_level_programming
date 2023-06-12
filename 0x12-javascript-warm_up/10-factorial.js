#!/usr/bin/node
const args = process.argv.slice(2);
let factorial = 1;
if (isNaN(args[0])) {
  console.log(factorial);
} else {
  let x = Number(args[0]);
  while (x > 1) {
    factorial *= x;
    x--;
  }
  console.log(factorial);
}
