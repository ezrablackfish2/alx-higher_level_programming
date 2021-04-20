#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing number of occurrences');
}

else {
	let x = Number(process.argv[2]);
	while (x != 0) {
		console.log('C is fun');
		x -= 1;
	}
}
