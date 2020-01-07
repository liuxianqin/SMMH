#include<iostream>

using namespace std;


int fib(int n){
    return (2>n)? n : fib(n-1)+fib(n-2);
}


int main(){

    for(int i = 0; i<64 ;i++)
        cout << fib(i) <<endl;
    cout<<fib(4)<<endl;
    return 0;
}