#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const arg = process.argv[2];
  if (arg > 0) {
    for (let i = 0; i < arg; i++) {
      let out = '';
      for (let j = 0; j < arg; j++) {
	out += 'X'
      }
      console.log(out);
    }
  }
}
