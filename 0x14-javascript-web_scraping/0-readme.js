#!/usr/bin/node
const fs = require("fs");

if (!process.argv[2]) {
	console.log("please insert a file name");
	return;
}


const path = `./${process.argv[2]}`;

fs.readFile(path, "utf8", (err, data) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(data);

});

