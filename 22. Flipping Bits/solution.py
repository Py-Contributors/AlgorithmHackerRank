'''
    Topic : Algorithms
    Subtopic : Flipping bits
    Language : Python3
    Problem Statement :
        You will be given a list of 32 bit unsigned integers. Write a function to Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.
    Url : https://www.hackerrank.com/challenges/flipping-bits/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

BITS = pow(2, 32) - 1


def flippingBits(n):
    # Write your code here
    return BITS ^ n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
