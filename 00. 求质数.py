#incoding:utf-8
#num:为传入数，判断该数是否为质数
def prime(num):
	if num <2:
		return False

	for i in range (2,num):
		if num%i==0:
			return False
	return True

if __name__=="__main__":
	box=[]
	for i in range (1,1001):
		if prime(i)==True:
			box.append(i)
	print box