'''
    Topic : Algorithms
    Subtopic : SimpleArraySum
    Language : Python
    Problem Statement : Print the sum of the array's elements as a single integer.
    Url : https://www.hackerrank.com/challenges/simple-array-sum/problem
'''
#!/bin/python3

# Complete the simpleArraySum function below.
#
def simpleArraySum(ar:list):
    return(sum(ar))

if __name__ == '__main__':
    userInput = input("Enter comma seprated value : ").strip()
    ar = list(map(int, userInput.rstrip().split(',')))
    result = simpleArraySum(ar)
    print(result)