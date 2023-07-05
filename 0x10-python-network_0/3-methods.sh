#!/bin/bash
# Sciript to show all available methods
curl -sI "$1" | grep Allow | sed "s/Allow: //"
