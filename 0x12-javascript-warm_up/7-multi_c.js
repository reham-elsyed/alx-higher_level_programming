#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const i = Number(process.argv[2]);
  let n = 0;
  while (n < i) {
    console.log('C is fun');
    n++;
  }
}
