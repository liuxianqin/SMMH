#coding=utf-8

import random
import time


class JCB:
	def __init__(self):
		self.job_name=random.randint(1000,9999)
		self.submit_time=random.randint(0,10)
		self.need_time=random.randint(1,20)
		self.ratio=1
		self.wait_time=0
		self.finish_time=0
		self.status="Wait"
	
	def __str__(self):
		return str(self.job_name)+"\t"+str(self.need_time)+"\t\t"+self.status+"\t\t"+str(self.submit_time)




