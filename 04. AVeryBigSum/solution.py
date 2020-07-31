'''
    Topic : Algorithms
    Subtopic : A Very Big Sum
    Language : Python
    Problem Statement : 
        Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
        aVeryBigSum has the following parameter(s):
        ar: an array of integers .
        
    Url :https://www.hackerrank.com/challenges/a-very-big-sum/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
the range is 0 through 4,294,967,295 (232 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−231) through 2,147,483,647 (231 − 1) for representation as two's complement.
'''