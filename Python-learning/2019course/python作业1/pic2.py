#coding=utf-8

print("2.1 for")
for i in range(1,8):
	if i>4:
		print("*"*(8-i))
		continue
	print("*"*i)

temp=5
print("2.2 for")
for i in range(1,8):
	#temp=5
	if i>4:
		print(" "*(i-4)+"*"*(temp))
		temp-=2
		continue	

	print(" "*(4-i) + "*"*(2*i-1))


print("2.3 while")
n=5
n=int(n)
m=t=2*n-1    #双重赋值
while m>=1:
    if(m==t or m==1):#打印第一行和最后一行
        print('  '*n + '*' + '  '*4*(n-1))
    elif(m>=n):#打印下半部分
        print('  '*(m-n+1)+'*'+'  '*(2*(t-m)-1)+' *')
    else:#打印上半部分
        print('  '*(n-m+1)+'*'+'  '*(2*m-3)+' *')
    m-=1

