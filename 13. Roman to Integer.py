#incoding:utf-8
#roman:传入的罗马值
def change(roman):
	dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	box=[]
	a=[]
	
	for i in range(len(roman)):
		box.append(dic[roman[i]])
	print box
	

	i=0
	while i<len(box)-1:
		sum1=box[i]
		for j in range(i+1,len(box)):

			print i,j
			if box[i]!=box[j]:
				a.append(sum1)
				break
			else:
				sum1=sum1+box[j]
				if j==len(box)-1:
					a.append(sum1)
		i=j
        print a
if __name__=="__main__":
	change('DCCCLVV')