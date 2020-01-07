#include<iostream>

using namespace std;

int hailstone(int n){
	int count = 1;
	while(n>1){
	n%2==1 ? n=3*n+1 : n/=2;count ++;
	}
	return count;
}

int main(){
	cout<<hailstone(64)<<endl;
	cout<<hailstone(17)<<endl;
	cout<<endl;
	return 0;
}
