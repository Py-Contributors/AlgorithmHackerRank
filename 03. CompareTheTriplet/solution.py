'''
    Topic : Algorithms
    Subtopic : Compare The Triplet
    Language : Python
    Problem Statement :Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.

        compareTriplets has the following parameter(s):
            a: an array of integers representing Alice's challenge rating
            b: an array of integers representing Bob's challenge rating

    Url : https://www.hackerrank.com/challenges/compare-the-triplets/problem
'''
def compareTriplets(a:list, b:list):
    aliceScore = 0
    bobScore = 0
    for i in range(len(a)):     
        if a[i] > b[i]:
            aliceScore += 1
        elif b[i] > a[i]:
            bobScore += 1
    return [aliceScore,bobScore]

a = [5,6,7]
b = [3,6,10]
answer = compareTriplets(a,b)
print(answer)
# >>> [1, 1]