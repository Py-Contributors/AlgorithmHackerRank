'''
    Topic : Algorithms
    Subtopic :MiniMax Sum
    Language : Python
    Problem Statement :
        Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

        For example,arr=[1,3,5,7,9] . Our minimum sum is 1+3+5+7=16 and our maximum sum is 3+5+7+9=24. 

    Url : https://www.hackerrank.com/challenges/mini-max-sum/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:]))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
