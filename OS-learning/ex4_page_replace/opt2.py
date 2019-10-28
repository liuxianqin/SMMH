#coding=utf-8

class opt:
	def __init__(self,MSIZE,ins_list,pages):
		self.msize=MSIZE
		self.stack=[]
		self.ins_list=ins_list
		self.pages=pages
		
	
	def run(self):
		for i in range(self.msize):
			self.stack.append(self.pages[(self.ins_list[i]//10)])
		print(self.stack)
		for i in self.ins_list[self.msize:]:
			print(i)



if __name__=="__main__":
	pass
		
