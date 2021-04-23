#!/usr/bin/node

exports.esrever = function (list) {
	let len = list.length - 1;
	let i = 0;
	let temp = 0;
	while (len >= i) {
		temp = list[i];
		list [i] = list[len];
		list[len] = temp;
		len -= 1;
		i += 1;
	}
	return (list);
}
