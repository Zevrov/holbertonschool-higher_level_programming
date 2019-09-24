#!/usr/bin/node

const tasks = require('request');

tasks.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
  }

  const product = {
  };

  for (const task of body) {
    if (task.completed === true) {
      if (product[task.userId] === undefined) {
        product[task.userId] = 0;
      }
      product[task.userId]++;
    }
  }

  console.log(product);
});
