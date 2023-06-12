#!/usr/bin/node
function factor (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factor(n - 1);
}
const args = process.argv.slice(2);
let factorial = 1;
if (isNaN(args[0])) {
  console.log(factorial);
} else {
  const x = Number(args[0]);
  factorial = factor(x);
  console.log(factorial);
}
