/*
    Topic : Algorithms
    Subtopic : Pairs
    Language : C++
    Problem Statement :
        Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
    Url : https://www.hackerrank.com/challenges/pairs/problem
*/
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'pairs' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY arr
 */

int pairs(int k, vector<int> arr) {
    map <int, int> m;
    for(int x : arr)
    {
        m[x]++;
    }
    int c = 0;
    int i;
    for(i = 0; i < arr.size(); i++)
    {
        m[arr[i]]--;
        if(m[k + arr[i]] > 0)
        {
            c++;
        }
        m[arr[i]]++;
    }
    return(c);
}
