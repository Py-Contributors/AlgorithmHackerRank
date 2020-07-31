'''
    Topic : Algorithms
    Subtopic : Plus Minus
    Language : Python
    Problem Statement : 
        Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

    Url : https://www.hackerrank.com/challenges/plus-minus/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    countPositive = 0
    countNegative =0
    for i in range(n):
        if arr[i] > 0:
            countPositive += 1 
        elif arr[i] < 0:
            countNegative += 1
    countZero = n - countPositive-countNegative
    print(countPositive/n)
    print(countNegative/n)
    print(countZero/n)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
