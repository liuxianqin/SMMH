#coding=utf-8
from JCB import JCB

class fcfs:
	def __init__(self,jcb_list):
		self.timeline=0
		self.jlist=jcb_list
		self.jlist=sorted(self.jlist, key=lambda jcb: jcb.submit_time)
		self.turnover=[]
		self.weight_turnover=[]
		self.a_turnover=0
		self.a_weight_turnover=0
	
	def working(self):
		print("**********先来先服务********")
		self.timeline=self.jlist[0].submit_time
		for i in range(len(self.jlist)):
			#self.timeline+=self.jlist[i].need_time
			self.jlist[i].finish_time=self.timeline+self.jlist[i].need_time
			self.timeline+=self.jlist[i].need_time
			self.turnover.append(self.timeline-self.jlist[i].submit_time)
			self.weight_turnover.append(self.turnover[-1]/self.jlist[i].need_time)
			print("作业id"+"\t"+"提交时刻"+"\t"+"需要时间"+"\t"+"完成时刻"+"\t"+"周转时间"+"\t"+"带权周转时间" )
			print(str(self.jlist[i].job_name)+"\t"+str(self.jlist[i].submit_time)+"\t\t"+str(self.jlist[i].need_time)+"\t\t"+str(self.jlist[i].finish_time)+"\t\t"+str(self.turnover[-1])+"\t\t"+str(self.weight_turnover[-1]))
			self.jlist[i].status="finish"
	
	def print_result(self):
		for i in self.turnover:
			self.a_turnover+=i
		self.a_turnover/=len(self.jlist)
		for i in self.weight_turnover:
			self.a_weight_turnover+=i
		self.a_weight_turnover/=len(self.jlist)
		print("平均周转时间"+"\t"+"平均带权周转时间")
		print(str(self.a_turnover)+"\t\t"+str(self.a_weight_turnover))
		
		
		

'''

if __name__=="__main__":
	jlist=[]
	for i in range(6):
		i=JCB()
		jlist.append(i)
	test=fcfs(jlist)
	test.working()
	test.print_result()
'''			
			
			
			
