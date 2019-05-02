#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(sys.argv) == 1:
        print('{} arguments.'.format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print('{} argument:'.format(len(sys.argv) - 1))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print('{:d}: {:s}'.format(i, sys.argv[z]))
