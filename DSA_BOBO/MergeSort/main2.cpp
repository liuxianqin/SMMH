#include<iostream>
#include"mergeSort.h"
#include"SortTestHelper.h"
using namespace std;

template<typename T>
void mergeSortBU(T arr[],int n){
    for(int sz=1;sz<=n;sz+=sz)
        for(int i=0;i+sz<n ;i+=sz+sz){
            __merge(arr,i,i+sz-1,min(i+sz+sz-1,n-1));
        }
}


int main(){
    int n=5000;
    int* arr1=SortTestHelper::generateRandomArray(n,0,n);
   

    SortTestHelper::testSort("Merge Sort",mergeSort,arr1,n);
    
    
    delete[] arr1;
   
    return 0;
}