#coding=utf-8

import random 
from collections import deque
import time
#tty [-s][--help][--version]
class PCB:
	def __init__(self):
		
		#status: ready  running finish
		
		self.pid=random.randint(1000,9999)
		self.priorty=random.randint( 1,20 )
		self.need_cpu_time=random.randint( 1,20)
		self.status="ready"
		
	def __str__(self):
		return str(self.pid)+"\t"+self.status+"\t"+str(self.priorty)+"\t"+str(self.need_cpu_time)

class PriorityAlgorithm:
	def __init__(self,n):
		self.ready_list=[]
		for pcb in range(n):
			pcb=PCB()
			self.ready_list.append(pcb)
		self.ready_list=sorted(self.ready_list, key=lambda pcb: pcb.priorty)
	def print_format(self):
		print("当前就绪队列:")
		print("pid"+"\t"+"状态"+"\t"+"优先级"+"\t"+"剩余时间")
		for i in range(len(self.ready_list)):
			print(self.ready_list[i])
	
#	def sort_list(self):
#		sorted(self.ready_list, key=lambda pcb: pcb.priorty)
	def working(self):
		while len(self.ready_list)>0:
			print("时间片到")
			self.ready_list[-1].priorty-=3
			if self.ready_list[-1].priorty<0:
				self.ready_list[-1].priorty=0
			self.ready_list[-1].need_cpu_time-=1
			if self.ready_list[-1].need_cpu_time==0:
				self.ready_list.pop(-1)
			else:
				self.ready_list=sorted(self.ready_list, key=lambda pcb: pcb.priorty)
			self.print_format()
				
			
			
			
				












'''

if __name__=="__main__":
	test=PriorityAlgorithm(4)
	#test.sort_list()
	test.print_format()
	test.working()
		
'''
