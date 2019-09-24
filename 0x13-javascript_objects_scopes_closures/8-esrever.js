#!/usr/bin/node
exports.esrever = function (list) {
  const ret = Array(list.length);
  for (let index = list.length - 1, count = 0; index >= 0; index--, count++) {
    ret[count] = list[index];
  }
  return ret;
};
