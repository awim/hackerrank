#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    level = 0
    valleys = 0
    
    for move in s:
        if move == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1

    return valleys


""" if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
 """