#coding=utf-8

from jcb1 import JCB
import time
import random


class sjf:
	def __init__(self,jlist):
		self.jlist=jlist
		self.jlist=sorted(self.jlist, key=lambda jcb: jcb.submit_time)
		#tem=self.jlist[0].submit_time
		#self.timeline=tem
		#self.timeline_r1=tem
		#self.timeline_r2=tem
		self.clist=[]
		self.r1list=[]
		self.r2list=[]
		self.turnover=[]
		self.w_turnover=[]
		#self.slice=1
		print("作业创建时间排序：")
		print("作业名称"+"\t"+"提交时间"+"\t"+"CPU时间"+"\t\t"+"总时间"+"\n")
		for i in self.jlist:
			print(i.do_list)
				
	def working(self):
		while len(self.jlist)>0:
			for i in self.jlist:
				if i.do_list[0]=='cpu':
					self.clist.append(i)
				if i.do_list[0]=='r1':
					self.r1list.append(i)
				if i.do_list[0]=='r2':
					slef.r2list.append(i)
			
					
					
		
			
	



if __name__=="__main__":
	jlist=[]
	for i in range(5):
		i=JCB()
		jlist.append(i)
	for i in jlist:
		print(i)
	jlist[0].do_list=['cpu','r1','r2']
	jlist[1].do_list=['r1','r2','cpu']
	jlist[2].do_list=['cpu']
	jlist[3].do_list=['cpu','r1','r2']
	jlist[4].do_list=['r2','cpu','r1']
	
	
	
	test=sjf(jlist)
	#test.working()
	
	for i in test.jlist:
		print(i.do_list)
