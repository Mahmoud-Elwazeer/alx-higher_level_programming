#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  let i = 2;
  while (process.argv[i] !== undefined) {
    console.log(process.argv[i]);
    i++;
  }
}
