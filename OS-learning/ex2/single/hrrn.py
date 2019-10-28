#coding=utf-8
from JCB import JCB

class hrrn:
	def __init__(self,jcb_list):
		self.timeline=0
		self.jlist=jcb_list
		self.jlist=sorted(self.jlist, key=lambda jcb: jcb.submit_time)
		self.turnover=[]
		self.weight_turnover=[]
		self.a_turnover=0
		self.a_weight_turnover=0
		self.original_n=len(self.jlist)
		
	def working(self):
		print("**********最高响应比********")
		self.timeline=self.jlist[0].submit_time
		while len(self.jlist)>0:
			for i in self.jlist:
				i.ratio=(self.timeline-i.submit_time+i.need_time)/i.need_time
		
			self.jlist=sorted(self.jlist, key=lambda jcb: jcb.ratio)
			print("\n现在的响应比:")
			for i in self.jlist:
				print(str(i.job_name)+":"+str(i.ratio))
			print(">>>>>>>>>>>>")
			#self.timeline+=self.jlist[i].need_time
			self.jlist[-1].finish_time=self.timeline+self.jlist[-1].need_time
			self.timeline+=self.jlist[-1].need_time
			self.turnover.append(self.timeline-self.jlist[-1].submit_time)
			self.weight_turnover.append(self.turnover[-1]/self.jlist[-1].need_time)
			print("作业id"+"\t"+"提交时刻"+"\t"+"需要时间"+"\t"+"完成时刻"+"\t"+"周转时间"+"\t"+"带权周转时间" )
			print(str(self.jlist[-1].job_name)+"\t"+str(self.jlist[-1].submit_time)+"\t\t"+str(self.jlist[-1].need_time)+"\t\t"+str(self.jlist[-1].finish_time)+"\t\t"+str(self.turnover[-1])+"\t\t"+str(self.weight_turnover[-1]))
			self.jlist[-1].status="finish"
			self.jlist.pop(-1)
	
	def print_result(self):
		for i in self.turnover:
			self.a_turnover+=i
		self.a_turnover/=self.original_n
		for i in self.weight_turnover:
			self.a_weight_turnover+=i
		self.a_weight_turnover/=self.original_n
		print("平均周转时间"+"\t"+"平均带权周转时间")
		print(str(self.a_turnover)+"\t\t"+str(self.a_weight_turnover))
		
		
		



if __name__=="__main__":
	jlist=[]
	for i in range(6):
		i=JCB()
		jlist.append(i)
	test=hrrn(jlist)
	test.working()
	test.print_result()
			
			
			
			

