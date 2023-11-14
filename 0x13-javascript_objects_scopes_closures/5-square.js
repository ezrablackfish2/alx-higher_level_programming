#!/usr/bin/node

class Rectangle {
	constructor (w) {
		this.width = w;
	}

	print() {
		let h = this.width;
		while (h) {

		let w = this.width;
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
		this.width *= 2;
	}
}

module.exports = Rectangle;
