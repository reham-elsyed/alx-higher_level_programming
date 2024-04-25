#!/bin/bash
#Bash script that takes in a URL as an argument
curl -s "$1" GET -H "X-HolbertonSchool-User-Id:98"
