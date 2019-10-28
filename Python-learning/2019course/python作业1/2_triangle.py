#coding=utf-8


abc=list(map(int,input("input a b and c:").split(" ")))


if abc[0]+abc[1]>abc[2] and  abc[1]+abc[2]>abc[0]  and abc[2]+abc[0]>abc[1]:
	p=0.5*(abc[0]+abc[1]+abc[2])
	print('能构成三角形 面积是 %f' % (p*(p-abc[0])*(p-abc[1])*(p-abc[2])   )**0.5  )
else:
	 print("不能构成三角形")

