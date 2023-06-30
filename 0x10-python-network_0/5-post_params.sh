#!/bin/bash
#Make a post request and atttach some parameters
curl -s -X POST "email=test@gmail.com&subject=I will always be here for PLD" $1
