#!/usr/bin/node
exports.esrever = function (list) {
  const ret = Array(list.length);
  for (let index = list.length - 1; index >= 0; index--) {
    ret.push(ret[index]);
  }
  return ret;
};
