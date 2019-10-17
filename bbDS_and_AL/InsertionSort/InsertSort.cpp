#include<iostream>
#include"SortTestHelper.h"

using namespace std;

template<typename T>
void insertionSort(T arr[],int n ){
    for(int i=1;i<n;i++){
        T e=arr[i];
        int j;
        for( j=i;j>0 && arr[j-1]>e;j--){
            arr[j]=arr[j-1];
        }
        arr[j]=e;
    }
}

int main(){
    int n=10000;
    int *arr=SortTestHelper::generateRandomArray(n,0,n);
    int *arr3=SortTestHelper::generateNearlyOrderedArray(n,10);
    int *arr2=SortTestHelper::copyIntArray(arr,n);

    SortTestHelper::testSort("insertionSort",insertionSort,arr3,n);
    

    delete[] arr;
    delete[] arr2;
    return 0;

}