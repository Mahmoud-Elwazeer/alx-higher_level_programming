#!/usr/bin/code

exports.esrever = function (list) {
  let out = [];
  size = list.length;
  for (let i = size - 1; i >= 0; i--) {
    out.push(list[i]);
  }
  return (out);
};
