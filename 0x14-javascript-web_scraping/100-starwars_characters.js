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
  const dd = data.characters;
  for (const i of dd) {
    request.get(i, function (error, resp, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
