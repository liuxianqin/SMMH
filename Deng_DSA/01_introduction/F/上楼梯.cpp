#include<iostream>

using namespace std;


long long fib(int n){
    long long f = 0,g = 1;
    while (0<n--){
        g = g+f;
        f = g-f;
    }
    return g;
}


int main(){

    for(int i = 0; i<128 ;i++)
        cout << i << " : "<< fib(i) <<endl;
    cout<<fib(4)<<endl;
    return 0;
}