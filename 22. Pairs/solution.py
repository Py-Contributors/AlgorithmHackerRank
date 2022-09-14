'''
    Topic : Algorithms
    Subtopic : Pairs
    Language : Python 3
    Problem Statement :
        Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
    Url : https://www.hackerrank.com/challenges/pairs/problem
'''
#!/bin/python3

import os

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    m = {}
    for _ in arr:
        if(_ not in m.keys()):
            m[_] = 1
        else:
            m[_] += 1
    c = 0
    for i in range(len(arr)):
        if((k + arr[i]) in m.keys()):
            if(m[k + arr[i]] > 0):
                c += 1
        m[arr[i]] += 1
    return(c)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
