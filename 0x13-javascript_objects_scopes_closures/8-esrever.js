#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let cnt = 0;
  while ((len - cnt) > 0) {
    const temp = list[len];
    list[len] = list[cnt];
    list[cnt] = temp;
    cnt++;
    len--;
  }
  return list;
};
