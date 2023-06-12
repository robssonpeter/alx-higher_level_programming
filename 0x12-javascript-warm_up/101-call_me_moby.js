#!/usr/bin/node
exports.callMeMoby = function (n, funct) {
  for (let x = 0; x < n; x++) {
    funct();
  }
};
