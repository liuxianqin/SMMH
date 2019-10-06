#coding=utf-8
from JCB import JCB
from fcfs import fcfs
from sjf import sjf
from hrrn import hrrn




if __name__=="__main__":
	n=int(input("输入作业总数:"))
	jlist=[]
	for i in range(n):
		i=JCB()
		jlist.append(i)
	print("测试用例：")
	print("作业id"+"\t"+"需要时间"+"\t"+"状态"+"\t"+"提交时刻")
	for i in jlist:
		print(i)
	test1=fcfs(jlist)
	test1.working()
	test1.print_result()
	
	test2=sjf(jlist,n)
	test2.working()
	test2.print_result()
	
	test3=hrrn(jlist)
	test3.working()
	test3.print_result()
	print("*******************************\n\n")
	print("平均周转时间"+"\t"+"平均带权周转时间")
	print("FCFS:\t"+str(test1.a_turnover)+"\t"+str(test1.a_weight_turnover))
	print("SJF:\t"+str(test2.a_turnover)+"\t"+str(test2.a_weight_turnover))
	print("HRRN:\t"+str(test3.a_turnover)+"\t"+str(test3.a_weight_turnover))
	
	
	
