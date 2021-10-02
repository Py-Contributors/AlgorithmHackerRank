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

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    """ find the minimum and maximum values that can be calculated by summing exactly four of the five integers """
    arr = sorted(arr)
    return sum(arr[:-1]), sum(arr[1:])

assert miniMaxSum([1, 3, 5, 7, 9]) == (16, 24)
assert miniMaxSum([1, 2, 3, 4, 5]) == (10, 14)
assert miniMaxSum([5, 1, 1, 5]) == (7, 11)
assert miniMaxSum([1, 1, 1, 1, 1]) == (4, 4)
