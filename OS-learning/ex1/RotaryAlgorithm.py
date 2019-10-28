#coding=utf-8

import random

class PCB:
	def __init__(self):
		self.pid=random.randint(1000,9999)
		self.need_time=random.randint(1,20)
		self.rotary=random.randint(1,4)
		self.used_time=0
		self.status="ready"
	
	def __str__(self):
		return str(self.pid)+"\t"+self.status+"\t"+str(self.need_time)+"\t\t"+str(self.used_time)+"/"+str(self.rotary)




class RotaryAlgorithm:
	def __init__(self,n):
		self.ready_list=[]
		for pcb in range(n):
			pcb=PCB()
			self.ready_list.append(pcb)
	def print_list(self):
		print("时间片完 当前就绪队列:")
		print("pid"+"\t"+"状态"+"\t"+"还需时间片"+"\t"+"已用时间片/轮转时间片")
		for pcb in self.ready_list:
			print(pcb)
	
	def working(self):
		while len(self.ready_list)>0:
			#running
			self.ready_list[0].used_time+=1
			self.ready_list[0].need_time-=1
			self.print_list()
			if self.ready_list[0].need_time==0:
				self.ready_list.pop(0)
			if self.ready_list[0].used_time==self.ready_list[0].rotary:
				self.ready_list[0].used_time=0
				temp=self.ready_list.pop(0)
				self.ready_list.append(temp)
			if len(self.ready_list)==1 and self.ready_list[0].need_time==1:
				self.ready_list[0].need_time=0
				self.ready_list[-1].status="finish"
				print("********")
				self.print_list()
				print("就绪队列是空的")
				exit()
			
		
		
		
	
	

if __name__=="__main__":
	test=RotaryAlgorithm(5)
	test.print_list()
	test.working()

