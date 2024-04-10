#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
	let inst = 0;
	let element = 0;
	while (element < list.length) {
		if (list[element] === searchElement) {
			inst++;
		}
		element++;
	}
	return inst;
}
