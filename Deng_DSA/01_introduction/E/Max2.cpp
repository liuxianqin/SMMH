// 在区间A[lo,hi)中找出两个最大的整数A[x1] A[x2]

#include <iostream>

using namespace std;


void max2(int A[],int lo,int hi,int & x1,int & x2){
    for(x1 = lo, int i = lo + 1; i < hi; i++)
        if( A[x1] < A[i] ) x1 = i;
    for(x2 = lo, int i = lo + 1;i < x1;i++)
		if( A[x2] < A[i] ) x2 = i;
	for(int i = x1+1;i<hi ;i++)
		if( A[x2] < A[i] ) x2 = i;
}


int main(){
	
	int A[] = [1,2,3,4];
	max2(A,0,3);
    return 0;
}
