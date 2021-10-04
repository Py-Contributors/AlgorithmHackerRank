'''
    Topic : Algorithms
    Subtopic : Plus Minus
    Language : Python
    Problem Statement : 
        Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

    Url : https://www.hackerrank.com/challenges/plus-minus/problem
'''
#!/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr):
    countPositive = 0
    countNegative =0
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            countPositive += 1 
        elif arr[i] < 0:
            countNegative += 1
    countZero = n - countPositive-countNegative
    print("Count Positive:", countPositive/n)
    print("Count Negative:", countNegative/n)
    print("Count Zero:", countZero/n)
    
plusMinus([-4, 3, -9, 0, 4, 1])
