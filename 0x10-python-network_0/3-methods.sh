#!/bin/bash
# list the methods on a remote source
curl -Is "$1" | grep "Allow" | cut -d ' ' -f 2-
