#include<iostream>
#include"quickSort.h"
#include"quickSort2.h"
#include"SortTestHelper.h"
using namespace std;

int main(){
    int n=100000;
    int *arr1=SortTestHelper::generateRandomArray(n,0,n);
    int *arr2=SortTestHelper::copyIntArray(arr1,n);

    

    arr1=SortTestHelper::generateRandomArray(n,0,10);//大e量重复键值
    SortTestHelper::testSort("Quick Sort 0-10",quickSort,arr1,n);
    SortTestHelper::testSort("2 way QuickSort",quickSort2,arr2,n);

    
    delete[] arr1;
    delete[] arr2;
    return 0;
}