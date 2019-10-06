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
		#self.need_cpu_time=random.randint(1,9)
		#self.need_io_time=random.randint(1,6)
		#self.total_need_time=self.need_cpu_time+self.need_io_time
		self.status="Wait"
		#self.r1_time=random.randint(1,5)
		#self.r2_time=random.randint(1,5)
		
		self.do_list={}
		self.need_cpu_time=0
		self.need_r1_time=0
		self.need_r2_time=0
		self.total_need_time=self.need_cpu_time+self.need_r1_time+self.need_r2_time
		
	
	def __str__(self):
		return str(self.job_name)+"\t"+str(self.submit_time)+"\t"+str(self.need_cpu_time)+"\t"+str(self.total_need_time)
		
		
if __name__=="__main__":
	jlist=[]
	for i in range(5):
		i=JCB()
		jlist.append(i)
	#修改jcb，添加运行的方式。
	jlist[0].do_list['r1']=2
	jlist[0].do_list['cpu']=random.randint(1,9)
	jlist[0].do_list['r2']=3
	
	jlist[1].do_list['cpu']=random.randint(3,6)
	jlist[1].do_list['r2']=1
	
	jlist[2].do_list['r1']=2
	jlist[2].do_list['r2']=2
	jlist[2].do_list['cpu']=random.randint(4,6)
	
	jlist[3].do_list['cpu']=random.randint(1,9)
	
	jlist[4].do_list['cpu']=random.randint(1,9)
	jlist[4].do_list['r2']=3
	jlist[4].do_list['r1']=2
	
	for i in jlist:
		print(i)
	print("******************")
	for i in jlist:
			if 'cpu' in i.do_list:
				i.need_cpu_time=i.do_list['cpu']
			if 'r1' in i.do_list:
				i.need_r1_time=i.do_list['r1']
			if 'r2' in i.do_list:
				i.need_r2_time=i.do_list['r2']
			i.total_need_time=i.need_cpu_time+i.need_r1_time+i.need_r2_time
	for i in jlist:
		print(i)
	
