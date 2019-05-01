#!/usr/bin/bash
for z in range(97, 123):
    if z != 101 and z != 113:
        print("{:c}".format(z), end="")
