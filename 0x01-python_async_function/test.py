#!/usr/bin/env python3

from random import randint
import time

def add(start, stop):
    for odd in range(start, stop + 1, 3):
        yield odd

def randn():
    time.sleep(3)
    return randint(1, 19)

def main():
    lis = [a for a in add(1, 10)]
    tpl = tuple(add(2, 9))
    print(lis, tpl)

if __name__ == "__main__":
    main()

