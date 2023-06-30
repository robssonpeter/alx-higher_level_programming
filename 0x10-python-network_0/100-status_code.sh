#!/bin/bash
#Script to return the status code of the request
curl -sI $1 | grep -oP "[0-9]{3}" | head -n 1
