#!/usr/bin/node
exports.logMe = function (item) {
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  } else { exports.logMe.count++; }
  console.log(`${exports.logMe.count}: ${item}`);
};
