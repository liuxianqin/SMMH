#coding=utf-8

import random
from opt import opt

def note():
	print("There are algorithms is the program:")
	print("1->Optimization algorithm")
	print("2->First in First out algorithm")
	print("3->Least recently used algorithm")
	print("4->Least frequently used algorithm")
	n=int(input("Select the algorithm number,please:")) 
	if n>5 or n<1:
		print("请重新输入")
	return n

def produce_addstream():
	#ori_list=[]
	#for i in range(320):
	#	ori_list.append(i)
	#print(ori_list)
	ins_list=[]
	time=0
	while time<319:
		start=random.randint(0,319)
		ins_list.append(start+1)
		fore=random.randint(0,start+1)
		ins_list.append(fore)
		ins_list.append(fore+1)
		back=random.randint(fore+2,319)
		ins_list.append(back)
		time+=4
	
	print(ins_list)
	print("***********************")
	#pages=[ori_list[i:i+10] for i in range(0,len(ori_list),10)]
	#for i in pages:
	#	print(i)
	
	return ins_list

def run():
	(ins_list,pages)=produce_addstream()
	#test=pages[ins_list[0]//10]
	#test=pages[(ins_list[0]//10)]
	#for i in ins_list:
	#	print(i in test)
			
    

if __name__=="__main__":
	#note()
	ori_list=[]
	for i in range(320):
		ori_list.append(i)
	pages=[ori_list[i:i+10] for i in range(0,len(ori_list),10)]
	ins_list=produce_addstream()
	print(ins_list)
	opt=opt(4,ins_list,pages)
	opt.run()
	#run()
	for MSIZE in range(4,32):
		n=note()
		
	
