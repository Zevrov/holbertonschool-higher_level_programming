#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    cnt = 0
    for z in range (1, len(argv)):
        cnt += int(argv[z])
    print(cnt)
