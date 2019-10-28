#coding=utf-8

layer=int(input("请输入层数"))

a=list(range(1,layer+1))
#print("".join(str(i) for i in a))


#for i in range(1,layer+1):
#	print( "*"*((layer-i)//2)+"&"*((layer-i)//2)             )

for i in range(1,layer+1):
	
	temp=list(range(1,i))
	temp2=list(range(i-1,0,-1))
#	print("".join(str(i) for i in temp))
#	print("".join(str(i) for i in temp2))
#	print("\n")
	print( " "*((2*layer-2*i)//2)+ ( "".join(str(i) for i in temp)) +str(i)+("".join(str(i) for i in temp2))  +" "*((2*layer-2*i)//2)) 
