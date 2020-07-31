/*
    Topic : Algorithms
    Subtopic :MiniMax Sum
    Language : C++
    Problem Statement :
        Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

        For example,arr=[1,3,5,7,9] . Our minimum sum is 1+3+5+7=16 and our maximum sum is 3+5+7+9=24. 

    Url : https://www.hackerrank.com/challenges/mini-max-sum/problem
*/
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the miniMaxSum function below.
void miniMaxSum(vector<int> arr) {

    long long min = LLONG_MAX , max = LLONG_MIN , sum ;
    for(int i = 0 ;i < arr.size() ; ++i)
    {
        sum = 0;
        for(int j = 0; j < arr.size() ; ++j)
        {
            if(i != j)
                sum += arr[j];
        }

        if(sum > max)
            max = sum;

        if (sum < min)
            min = sum;
    }

    cout << min << " " << max << endl;
}

int main()
{
    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(5);

    for (int i = 0; i < 5; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    miniMaxSum(arr);

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

