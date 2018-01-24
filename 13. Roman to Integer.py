#incoding:utf-8
#roman:传入的罗马值
def change(roman):
	dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	box=[]
	a=[]
	
	for i in range(len(roman)):
		box.append(dic[roman[i]])
	
	i=0
	while i<len(box)-1:
		num=box[i]
		for j in range(i+1,len(box)):

			if j==len(box)-1:
				if box[i]==box[j]:
					num=num+box[j]
					a.append(num)
				else:
					a.append(num)
					a.append(box[j])
			else:
				if box[i]==box[j]:
					num=num+box[j]
				else:
					a.append(num)
					break
		i=j
	
	b=[]
	
	if len(a)%2==0:
		i=0
	else:
		b.append(a[0])
		i=1

	while i<len(a)-1:
		if a[i]>=a[i+1]:
			b.append(a[i]+a[i+1])
		else:
			b.append(a[i+1]-a[i])
		i=i+2

	lastsum=0
	i=0
	for i in range(len(b)):
		lastsum=lastsum+b[i]
	print 'a:',a,'b:',b,lastsum



if __name__=="__main__":
	change('DCCCLVV')
	change('DCCCLV')
	change('CDIV')
	change('CDIVX')#不正确的写法
	change('CDXIV')
	change('DCVI')
	