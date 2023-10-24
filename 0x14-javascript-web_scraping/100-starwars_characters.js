#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request.get(API_URL + id, function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const p = data.characters;
  for (const i in p) {
    request.get(i, function (err, resp, body1) {
      if (err) {
        console.log(err);
      } else {
        const data1 = JSON.parse(body1);
        console.log(data1);
      }
    });
  }
});
