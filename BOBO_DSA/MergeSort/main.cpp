#include<iostream>
#include"mergeSort.h"
#include"InsertSort.h"


int main(){

    int n=5000;
    int* arr1=SortTestHelper::generateRandomArray(n,0,n);
    int* arr2=SortTestHelper::copyIntArray(arr1,n);

    SortTestHelper::testSort("Merge Sort",mergeSort,arr1,n);
    SortTestHelper::testSort("Insert Sort",insertionSort,arr2,n);
    
    delete[] arr1;
    delete[] arr2;
    return 0;
}