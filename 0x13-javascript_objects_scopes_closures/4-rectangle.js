#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		this.width = w;
		this.height = h;
	}

	print() {
		let h = this.height;
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
//                this.height *= 2;
                this.width *= 2;
		let h = this.height;
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
        rotate() {
		let tmp = this.width;
		this.width = 2 * this.height;
		this.height = tmp / 2;
                let h = this.height;
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

}

module.exports = Rectangle;
