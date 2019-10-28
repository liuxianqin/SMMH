#coding=utf-8
from PriorityAlgorithm import PriorityAlgorithm
from RotaryAlgorithm import RotaryAlgorithm


if __name__=="__main__":
	pcb_num=int(input("输入进程数:"))
	way=input("调度方法 A：优先权法 B：时间片法:")
	if way=="A":
		A=PriorityAlgorithm(pcb_num)
		A.working()
	if way=="B":
		B=RotaryAlgorithm(pcb_num)
		B.working()












