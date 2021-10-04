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

import os

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)
    
assert aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 5000000015
assert aVeryBigSum([1, 2, 3, 4, 5]) == 15
assert aVeryBigSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55

'''
the range is 0 through 4,294,967,295 (232 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−231) through 2,147,483,647 (231 − 1) for representation as two's complement.
'''