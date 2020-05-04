'''
    Topic : Algorithms
    Subtopic : Time Conversion
    Problem Statement :
        Complete the timeConversion function in the editor below. 
        It should return a new string representing the input time in 24 hour format.

    Url : https://www.hackerrank.com/challenges/time-conversion/problem
'''
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time = s.split(':')
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == '12':
            time[0] = '00'
    ntime = ':'.join(time)
    return str(ntime[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
