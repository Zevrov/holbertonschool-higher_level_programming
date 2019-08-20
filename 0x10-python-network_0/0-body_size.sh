#!/bin/bash
# displays body size of the response to a url request
curl -sI "$1" | grep "Content-Length" | cut -d " " -f 2
