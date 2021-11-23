#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const url = process.argv[2];
  const result = {};
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const arr = JSON.parse(body);
      for (let i = 0; i < arr.length; i++) {
        if (arr[i].completed === true) {
          if (result[arr[i].userId] === undefined) {
            result[arr[i].userId] = 1;
          } else {
            result[arr[i].userId] += 1;
          }
        }
      }
      console.log(result);
    }
  });
}
