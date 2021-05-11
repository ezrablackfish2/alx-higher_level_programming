#!/usr/bin/node
const request = require("request");

if (!process.argv[2]) {
	console.log("please insert a url");
	return;
}

url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`
id = process.argv[2]


request.get(url, (error, response) => {
	if (error) {
		console.error("Error:", error);
	}
	else {
		data = JSON.parse(response.body);
		console.log(data.title);
	}
});
