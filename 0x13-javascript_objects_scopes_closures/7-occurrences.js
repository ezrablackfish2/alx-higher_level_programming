#!/usr/bin/node

exports.nbOccurences = function (a, b) {
	let i;
	let rep = 0;
	for (i = 0; i < a.length; i++) {
		if (b === a[i]) {
			rep += 1;
		}
	}
	return(rep);
};
