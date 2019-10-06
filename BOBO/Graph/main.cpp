#include<iostream>
#include<vector>
#include"SparseGraph.h"
#include"DenseGraph.h"
using namespace std;





int main(){
    int N=20;
    int M=100;
    srand(time(NULL));

    SparseGraph g1(N,false);
    for(int i=0;i<M;i++){
        int a=rand()%N;
        int b=rand()%N;
        g1.addEdge(a,b);
    }

    for (int v=0;v<N;v++){
        cout<<v<<":";
        SparseGraph::adjIterator adj(g1,v);
        for (int w=adj.begin();!adj.end();w=adj.next())
            cout<<w<<" ";
        cout<<endl;
    }

    cout<<"**************************"<<endl;

    DenseGraph g2(N,false);
    for(int i=0;i<M;i++){
        int a=rand()%N;
        int b=rand()%N;
        g2.addEdge(a,b);
    }

    for(int v=0;v<N;v++){
        cout<<v<<":";
        DenseGraph::adjIterator adj(g2,v);
        for(int w=adj.begin();!adj.end();w=adj.next())
            cout<<w<<" ";
        cout<<endl;
    }

    vector<int> arr({1,2,3,4,5});
    vector<int>::iterator iter;
    for(iter=arr.begin();iter!=arr.end();iter++)
        cout<<*iter<<endl;

    cout<<"HEO"<<endl;
    return 0;
}