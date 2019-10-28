#coding=utf-8


day=int(input("第几天"))
count=int(input("还有多少个"))

for i in range(day-1,0,-1):
	if i==1:
                count*=4
                print(("第%d天还有 %d 个") % (i,count))	
                break
	count=(count+1)*2
	print(("第%d天还有 %d 个") % (i,count))	
#	if i==1:
#		count*=4
#		print(("第%d天还有 %d 个") % (i,count))
