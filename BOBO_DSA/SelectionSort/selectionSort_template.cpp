#include<iostream>
#include"student.h"
#include"SortTestHelper.h"
using namespace std;

template<typename T>

void selectionSort(T arr[],int n){
	for(int i=0;i<n;i++){
		//寸照[i,n)最小值
		int minIndex=i;
		for(int j=i+1;j<n;j++)
			if(arr[j]<arr[minIndex])
				minIndex=j;
		swap(arr[i],arr[minIndex]);
	}
}

int main(){
	int a[10]={10,3,5,6,8,2,1,7,4,9};
	selectionSort(a,10);
	for(int i=0;i<10;i++)
		cout<<a[i]<<" ";
	cout<<endl;

	string c[4]={"DDDDD","b","f","a"};
	selectionSort(c,4);
	for(int i=0;i<4;i++)
		cout<<c[i]<<" ";
	cout<<endl;
	 
	Student d[4]={{"d",90},{"a",80},{"e",30},{"f",230}};
	selectionSort(d,4);
	for(int i=0;i<4;i++)
		cout<<d[i];
	cout<<endl;
	
	int n=100000;
	int *arr=SortTestHelper::generateRandomArray(n,0,n);
	selectionSort(arr,n);
	SortTestHelper::printArray(arr,n);



	SortTestHelper::testSort("selection sort",selectionSort,arr,n);
	delete[] arr;


	return 0;
}


