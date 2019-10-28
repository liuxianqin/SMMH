
print("1.1  while")
char="*"
i=0
while i < 7:
	print(char)
	char+="*"
	i+=1




print("1.1  for")
for j in range(8):
	print("*"*j)


print("1.2 while")
i=5
while i>4 and i<10:
	print("*"*i)
	i+=1

#print("\n")
print("1.2 for")
for j in range(5,10):
	print("*"*j)	


print("1.3 while")
i=5
while i>0:
	print("*"*i)
	i-=1

#print("\n")
print("1.3  for")
for j in range(5,0,-1):
	print("*"*j) 


print("1.4 while")
i=0
while i<5:
	print((i*" ")+(5-i)*"*")
	i+=1

print("1.4  for")
for j in range(0,5):
	print((j*" ")+(5-j)*"*")
