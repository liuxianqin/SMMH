#ifndef HEAP_H
#define HEAP_H
#include<iostream>
#include<algorithm>
#include<ctime>
#include<cmath>
#include<string>
#include<cassert>

using namespace std;
template<typename Item>
class IndexMaxHeap{

private:
    Item* data;
    int* indexs;
    int capacity;
    int count;
    void shiftUp(int k){
        while(k>1 && data[indexs[k/2]]<data[indexs[k]]){
            swap(indexs[k/2],indexs[k]);
            k/=2;
        }
    }
    void shiftDown(int k){
        //条件：有左孩子
        while(2*k<=count){

            int j=2*k;
            if(j+1<=count && data[indexs[j+1]]>data[indexs[j]])
                j+=1;
            if(data[indexs[k]]>=data[indexs[j]])
                break;
            swap(indexs[k],indexs[j]);
            k=j;
        }
    }

public:
    IndexMaxHeap(int capacity){
        data=new Item[capacity+1];
        indexs=new int[capacity+1]
        count=0;
        this->capacity=capacity;
    }

    IndexMaxHeap(Item arr[],int n){
        data=new Item[n+1];
        capacity=n;
        for(int i=0;i<n;i++)
            data[i+1]=arr[i];
        count=n;
        //一个性质
        for(int i=count/2;i>=1;i--)
            shiftDown(i);
    }

    int size(){
        return count;
    }

    int isEmpty(){
        return count==0;
    }

    void insert(int i,Item item){
        assert(count+1<=capacity);
        assert(i+1>=1 && i+1<=capacity);
        i+=1;
        data[i+1]=item;
        index[count+1]=i;
        count++;
        shiftUp(count);
    }

    Item extractMax(){
        assert(count>0);
        Item ret=data[indexs[1]];

        swap(indexs[1],indexs[count]);
        count--;
        shiftDown(1);
        return ret;
    }

    int extractMaxIndex(){
        assert(count>0);
        int ret=indexs[1]-1;

        swap(indexs[1],indexs[count]);
        count--;
        shiftDown(1);
        return ret;
    }

    Item getItem(int i){
        return data[i+1];
    }

    void change(int i,Item newItem){
        i+=1;
        data[i]=newItem;
        for(int j=1;i<=count;j++){
            if(indexs[j]==i){
                shiftUp(j);
                shiftDown(j);
                return;
            }
        }
    }


    void printHeap(){
        for(int i=1;i<this->count;i++){
            cout<<data[i]<<endl;
        }
    }

    ~IndexMaxHeap(){
        delete[] data;
        delete[] indexs;
    }
};



#endif 