#!/bin/python3

import math
import os
import random
import re
import sys

# Problems
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    m = 0
    i = 0
    l = len(c)
    
    while i < l:
        if i+2 < l and c[i+2] == 0:
            i = i+2
        else:
            i = i+1

        if i >= l:
            break 
        m += 1
    return m



""" if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close() """

c = [0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1]
print(jumpingOnClouds(c))