#!/bin/bash
# sends a POST request
curl -s -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
