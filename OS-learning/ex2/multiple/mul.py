#coding=utf-8

from jcb import JCB





if __name__=="__main__":
	n=int(input("进程个数:"))
	jlist=[]
	for i in range(n):
		jcb=JCB()
		jlist.append(jcb)
	
