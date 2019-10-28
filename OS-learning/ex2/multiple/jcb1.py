#coding=utf-8

import random
import time


class JCB:
	def __init__(self):
		'''
		资源种类 R1 R2
		cpu时间
		'''
		self.job_name=random.randint(1000,9999)
		self.submit_time=random.randint(0,10)
		self.cpu_time=random.randint(1,9)
		self.status="Wait"
		self.r1_time=random.randint(1,5)
		self.r2_time=random.randint(1,5)
		self.do_list=[]
		self.total_need_time=self.cpu_time+self.r1_time+self.r2_time
		
	
	def __str__(self):
		return str(self.job_name)+"\t\t"+str(self.submit_time)+"\t\t"+str(self.cpu_time)+"\t\t"+str(self.total_need_time)
		
		
if __name__=="__main__":
	jlist=[]
	for i in range(5):
		i=JCB()
		jlist.append(i)
	#修改jcb，添加运行的方式。
	


