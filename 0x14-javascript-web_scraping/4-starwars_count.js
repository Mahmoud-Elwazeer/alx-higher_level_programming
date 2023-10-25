#!/usr/bin/node

const process = require('process');
const args = process.argv;

const lst = args[2].split('/');
const src = lst[lst.length - 1];

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/people/18';

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  console.log(data[src].length);
});
