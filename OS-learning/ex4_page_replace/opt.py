#coding=utf-8

import random


def opt(msize,ins_list,pages):
	
	page_list=[]
	for i in ins_list:
		page_list.append(i//10)
	mirrors=[]
	
	fault=0
	for i in range(msize):
		
		mirrors.append(ins_list[i]//10)
		
	
	print(mirrors)
	for i in ins_list[msize:]:
		print(i)
		if i//10 not in mirrors:
			fault+=1
			print("page fault")
			#寻找未来第一次出现时候的下标里最大的  最长时间不被访问的
			#for j in ins_list[ ins_list.index(i):]:
			#对于之后还有的：
			for j in range(msize):
				if int(mirrors[j]) in page_list[ins_list.index(int(i)):]:
					a=ins_list[:].index(int(mirrors[j]))
					distances.append(a)
					
				else:
					print(1000000000)
				
			
				
				
	



def produce_addstream():
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
	
	#print(ins_list)
	#print("***********************")	
	return ins_list

    

if __name__=="__main__":
	#note()
	ori_list=[]
	for i in range(320):
		ori_list.append(i)
	pages=[ori_list[i:i+10] for i in range(0,len(ori_list),10)]
	ins_list=produce_addstream()
	print(ins_list)
	print(pages)
	
	opt=opt(4,ins_list,pages)
		
	

