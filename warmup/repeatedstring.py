#!/bin/python3

import math
import os
import random
import re
import sys

# Problem
# https://www.hackerrank.com/challenges/repeated-string/problem

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    a = len( [a for a in s if a == 'a'] )
    if n > l:
        d = int(n / l)
        m = n % l

        a = (d*a) + len( [a for a in s[0:m] if a == 'a'] )
    else:
        d = n - l
        a = len( [a for a in s[0:d] if a == 'a'] )

    return a


print repeatedString('ababa',3)
            


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     n = int(input())
#     result = repeatedString(s, n)
#     fptr.write(str(result) + '\n')
#     fptr.close()
