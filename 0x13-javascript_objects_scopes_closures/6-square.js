#!/usr/bin/node
const SquareOld = require('./5-square');

class Square extends SquareOld {
	charPrint(c) {
		let h = this.height;
		while (h) {
		let w = this.width;
		let str = '';
		while (w) {
			if (c) {
			str += c;
			}
			else {
				str += 'X';
			}
			w -= 1;
		}
		console.log(str);
			h -= 1;
		}
	}
}

module.exports = Square;
