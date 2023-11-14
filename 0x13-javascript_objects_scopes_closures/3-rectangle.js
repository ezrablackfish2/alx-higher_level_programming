#!/usr/bin/node

class Rectangle {
	constructor (w, h) {
		this.width = w;
		this.height = h;
	}
	print () {
		let h = this.height;
		while (h) {
		let str = '';
		let w = this.width;
		while (w) {
			str += 'X';
			w -= 1;
		}
		console.log(str);
		h -= 1;
	}
	}
}

module.exports= Rectangle;
