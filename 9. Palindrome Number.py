#incoding:utf-8
#num:传入的数字
def change(num):
	num=str(num)
	num=num[::-1]
	return num
def judge(num):
	if num<0:
		return False
	else:
		if str(num)==change(num):
			return True
		else:
			return False

if __name__=="__main__":
	print judge(123)
	print judge(-123)
	print judge(120)
	print judge(121)
	print judge(1)
	print judge(33)
