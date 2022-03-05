#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def after_sum(*args):
    if args:
        left = 0
        r = 0
        mult = 1
        flagl = False
        flagr = False
        for index, arg in enumerate(args):
            if arg == 0:
                if not flagl:
                    left = index
                    flagl = True
                elif not flagr:
                    r = index
                    flagr = True
        if not (flagr * flagl):
            return None
        else:
            for index, arg in enumerate(args):
                if (index > left) and (index < r):
                    mult = mult * arg
        return mult
    else:
        return None


if __name__ == "__main__":
    arguments = [int(i) for i in input().split()]
    arguments.reverse()
    print(after_sum(*arguments))
