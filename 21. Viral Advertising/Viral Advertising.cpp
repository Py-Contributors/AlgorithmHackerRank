#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n; //Taking input
    int resultwillbe = 2,likeaarecurrently = 2;
    //using for loop
    for(int i = 2; i <= n; i++){
        likeaarecurrently*=3; //Incrementing
        likeaarecurrently = likeaarecurrently/2;
        resultwillbe+=likeaarecurrently;
    }
    cout << resultwillbe << endl; //Printing Output
    return 0;
}