#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for z in dir(hidden_4):
        if not '__' in z:
            print(z)
