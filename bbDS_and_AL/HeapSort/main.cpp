#include<iostream>
#include<algorithm>
#include"heapSort.h"
#include"SortTestHelper.h"

using namespace std;


int main(){
    int n=1000000;
    int* arr1=SortTestHelper::generateRandomArray(n,0,n);
    int* arr2=SortTestHelper::copyIntArray(arr1,n);
    int* arr3=SortTestHelper::copyIntArray(arr1,n);

    SortTestHelper::testSort("Heap sort",heapSort1,arr1,n);
    SortTestHelper::testSort("Heap sort 2",heapSort2,arr2,n);
    SortTestHelper::testSort("Heap sort FINAL",heapSort,arr3,n);


    delete[] arr1;
    delete[] arr2;
    delete[] arr3;

}