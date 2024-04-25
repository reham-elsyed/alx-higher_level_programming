#!usr/bin/bash
# sriptsend request to url
curl -sI "$1" | grep "Content-length:" | cut -d' ' -f2
