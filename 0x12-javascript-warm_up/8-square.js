#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
}
else {
const i = Number(process.argv[2]);
	let n = 0;
	while ( n < i){
		console.log('X'.repeat(i));
		n++;
	}
}
