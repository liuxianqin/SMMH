#include<iostream>

using namespace std;

void selectionSort(int arr[],int n){
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
	return 0;
}


