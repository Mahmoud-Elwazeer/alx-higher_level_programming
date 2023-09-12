#!/usr/bin/node

exports.esrever = function (list) {
  const out = [];
  const size = list.length;
  for (let i = size - 1; i >= 0; i--) {
    out.push(list[i]);
  }
  list = out;
  return (list);
};
