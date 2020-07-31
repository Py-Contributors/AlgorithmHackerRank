/*
    Topic : Algorithms
    Subtopic : StairCase
    Language : C++
    Problem Statement : Write a program that prints a staircase of size 'n'.
    Url : https://www.hackerrank.com/challenges/staircase/problem
*/

#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n) {

    for(int i=0;i<n;i++) {
        cout << setfill(' ') << setw(n-(i+1)) << "";
        cout << setfill('#') << setw(i+1) << '#'<< endl;
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}

