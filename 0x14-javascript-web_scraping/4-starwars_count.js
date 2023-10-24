#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (!err) {
    const reslt = JSON.parse(body).reslt;
    console.log(
      reslt.reduce((count, movie) => {
        return movie.characters.find((character) => character.endWith('/18/'))
          ? count + 1
          : count;
      }, 0)
    );
  }
});
