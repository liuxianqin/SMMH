//最好情况 n-1
//最坏情况 2n-3
#include<algorithm>

void max2(int A[],int lo,int hi,int & x1,int & x2){
    if(A[x1 = lo] < A[x2 = lo+1]) swap(x1,x2);
    for(int i = lo + 2;i < hi; i++)
        if(A[x2]<A[i])
            if(A[x1] < A[x2=i])
                swap(x1,x2);