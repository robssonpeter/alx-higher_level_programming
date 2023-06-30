#!/bin/bash
# Script to find the content size of a response
curl -sI $1 | grep content-length | grep -o '[0-9]*'
