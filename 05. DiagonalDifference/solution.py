'''
    Topic : Algorithms
    Subtopic : Diagonal Difference
    Language : Python
    Problem Statement : Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    Url : https://www.hackerrank.com/challenges/diagonal-difference/problem
'''
#!/bin/python3
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    d1 = sum(arr[i][i] for i in range(n))
    d2 = sum(arr[i][n-i-1] for i in range(n))
    return abs(d1 - d2)


assert diagonalDifference([[11,2,4], [4,5,6], [10,8,-12]]) == 15
assert diagonalDifference([[1,2,3], [4,5,6], [9,8,9]]) == 2
assert diagonalDifference([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]) == 0
