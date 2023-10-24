#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(API_URL + id, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    const respjson = JSON.parse(body);
    console.log(respjson.title);
  } else {
    console.log('Error code: ' + resp.statusCode);
  }
});
