#incoding:utf-8
def output(inputA,inputB):
	box=inputA+inputB
	for i in range(len(box)-1):
		for j in range(i,len(box)):
			if box[i]>box[j]:
				box[i],box[j]=box[j],box[i]
	return box

if __name__=='__main__':
	print output([1,2,4],[1,3,4])

