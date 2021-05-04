#!/usr/bin/node
const fs = require("fs");

if (!process.argv[2]) {
	console.log("please insert a file name");
	return;
}



fs.writeFile(process.argv[2], process.argv[3], (err) => {
	if (err) {
		console.log("can not write file", err);
	} else {
	}
});

