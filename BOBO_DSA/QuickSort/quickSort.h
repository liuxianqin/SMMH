#ifndef QUICKSORT_H
#define QUICKSORT_H

#include<iostream>
using namespace std;
//前闭后闭

template<typename T>
int __partition(T arr[],int l,int r){
    swap(arr[l],arr[rand()%(r-l+1)+l]);
    T v=arr[l];
    //arr[l+1...j]<v;arr[j+1...i)>v
    int j=l;
    for(int i=l+1;i<=r;i++){
        if(arr[i]<v){
            swap(arr[j+1],arr[i]);
            j++;
        }
    }
    swap(arr[l],arr[j]);
    return j;
}

template<typename T>
void __quickSort(T arr[],int l,int r){
    if(l>=r)
        return;
    int p=__partition(arr,l,r);
    __quickSort(arr,l,p-1);
    __quickSort(arr,p+1,r);
}

template<typename T>
void quickSort(T arr[],int n){
    srand(time(NULL));
    __quickSort(arr,0,n-1);
}

#endif