#!/usr/bin/node
// write a text in a file
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) console.log(err);
});
