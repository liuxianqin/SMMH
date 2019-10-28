#coding=utf-8

from jcb1 import JCB
import time
import random


class fcfs:
	def __init__(self,jlist):
		self.jlist=jlist
		self.jlist=sorted(self.jlist, key=lambda jcb: jcb.submit_time)
		self.timeline=0
		self.turnover=[]
		self.w_turnover=[]
		
	def working(self):
		pass
	



if __name__=="__main__":
	jlist=[]
	for i in range(5):
		i=JCB()
		jlist.append(i)
	for i in range(5):
		print(i)
