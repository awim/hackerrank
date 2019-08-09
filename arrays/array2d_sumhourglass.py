#!/bin/python3

import math
import os
import random
import re
import sys

def midInRowSplit(splitter, arr):
    r = []
    m = int(splitter/2)
    l = len(arr)-2
    for i in range(l):
        r.append(arr[i+m])
    return r

def sumInRowSplit(splitter, arr):
    r = []
    l = len(arr)-2
    for i in range(l):
        r.append(sum(arr[i:i+splitter]))
    return r

# Complete the hourglassSum function below.
def hourglassSum(arr):
    _top, _mid, _bot = [], [], []
    _max = None

    l = len(arr)-2
    for i in range(l):
        _top = sumInRowSplit(3, arr[i])
        _mid = midInRowSplit(3, arr[i+1])
        _bot = sumInRowSplit(3, arr[i+2])

        print(_top)
        print(_mid)
        print(_bot)
        print('---------')

        
        for j,b in enumerate(_top):
            max = b + _mid[j] + _bot[j]
            if _max == None or max >= _max:
                _max = max

    return _max

        

""" if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close() """


arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

arr = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]

# arr = [
#     [-1, 1, -1, 0, 0, 0],
#     [0, -1, 0, 0, 0, 0],
#     [-1, -1, -1, 0, 0, 0],
#     [0, -9, 2, -4, -4, 0],
#     [-7, 0, 0, -2, 0, 0],
#     [0, 0, -1, -2, -4, 0]
# ]

print (hourglassSum(arr))