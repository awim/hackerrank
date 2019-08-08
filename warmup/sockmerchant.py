#!/bin/python3

import math
import os
import random
import re
import sys

# Problem
# https://www.hackerrank.com/challenges/sock-merchant/problem

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockSearch = {
        'color' : 0,
        'total' : 0,
        'match' : 0
    }
    sockSorted = []
    sock = ar[0]

    while(sock):
        if sockSearch not in sockSorted:
            sockSearch['color'] = sock
            sockSearch['total'] = len([  x for x in ar if x == sockSearch['color'] ])
            sockSearch['match'] = int (sockSearch['total'] / 2)
            sockSorted.append(sockSearch)

            while(sockSearch['color'] in ar):
                ar.remove(sockSearch['color'])

            if len(ar)>0:
                sock = ar[0]
                sockSearch = {}
        
        else:
            break
        
    #return sockSorted
    return sum( [ sock['match'] for sock in sockSorted if sock['match'] > 0 ] )
        


""" if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close() """

print(sockMerchant(9, [1,1,3,1,2,1,3,3,3,3]))
