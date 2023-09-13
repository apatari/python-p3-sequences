#!/usr/bin/env python3

def print_fibonacci(length):
    c = 0
    prev = 1
    temp = 0
    res = []
    for i in range(length):
            res.append(c)
            temp = c
            c += prev
            prev = temp

    print(res)