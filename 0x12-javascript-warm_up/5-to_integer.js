#!/usr/bin/node
if (process.argv[2] <= '9' && process.argv[2] >= '0') {
	console.log(`My number: ${process.argv[2]}`);
}
else {
	console.log('Not a number');
}
