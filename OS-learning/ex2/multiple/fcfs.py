#coding=utf-8

#添加特例： a先io后cpu提交早 b先cpu后io提交晚 处理机先执行哪一个？？？



#怎么刷新类
#如果两个作业同一时间申请同一个io资源，先创建的取得资源。

from jcb import JCB
import random
import time

class fcfs:
	def __init__(self,jlist):
		self.jlist=jlist
		#self.wait_list=jlist
		#self.ready_list=[]
		#self.ready_list=self.jlist
		self.timeline=0
		self.cpu_slice=1
		self.turnover=[]
		self.w_turnover=[]
		
		for i in jlist:
			if 'cpu' in i.do_list:
				i.need_cpu_time=i.do_list['cpu']
			if 'r1' in i.do_list:
				i.need_r1_time=i.do_list['r1']
			if 'r2' in i.do_list:
				i.need_r2_time=i.do_list['r2']
			i.total_need_time=i.need_cpu_time+i.need_r1_time+i.need_r2_time
		self.jlist=sorted(self.jlist, key=lambda jcb: jcb.submit_time)
		#for i in jlist:
		#	x=i.do_list.keys()
		#	print(list(x))    #有这个转换函数很ok
		#for i in jlist:
		#	tran=list(i.do_list.keys())
		#	print("%^%^%^%^%^")
		#	print(tran[0])
			
	def working(self):
		while len(self.jlist)>0:
			#如果第一个作业需要先io，等待第一个作业的io完成。
			if list(self.jlist.keys())[0]!='cpu':
				print(list(self.jlist.keys())[0])
			
			
			

				
				
				
				



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
	print("***************************")
	test=fcfs(jlist)
	test.working()
	
	for i in test.jlist:
		print(i)
	print("***************")
	for i in jlist:
		print(i)									#两个jlist不一样。
	
