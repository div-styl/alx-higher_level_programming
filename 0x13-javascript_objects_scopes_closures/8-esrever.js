#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length - 1;
  let cnt = 0;
  while ((len - cnt) > 0) {
    const temp = list[len - cnt];
    list[len - cnt] = list[cnt];
    list[cnt] = temp;
    cnt++;
  }
  return list;
};
