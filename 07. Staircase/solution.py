'''
    Topic : Algorithms
    Subtopic : StairCase
    Language : Python
    Problem Statement : Write a program that prints a staircase of size 'n'.
    Url : https://www.hackerrank.com/challenges/staircase/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1, n + 1):
        print(f'{"#"*i:>{n}}')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
