#!/usr/bin/node
exports.addMeMaybe = function(n, funct) {
  n++;
  funct(n);
};
