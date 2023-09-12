#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let out = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      out += 1;
    }
  }
  return (out);
};
