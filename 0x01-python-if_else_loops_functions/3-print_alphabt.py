#!/usr/bin/bash
for z in range(97, 123):
    if z != 113 and z != 101:
        print("{:c}".format(z), end="")
