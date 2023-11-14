#!/usr/bin/node

class Rectangle {
	constructor (size) {
		this.size = size;
	}

	print() {
		let h = this.size;
		while (h) {

		let w = this.size;
		let str = '';
		while (w) {
			str += 'X';
			w -= 1;
		}
		console.log(str);
		h -= 1;
		}
	}

	double() {
		this.size *= 2;
	}
}

module.exports = Rectangle;
