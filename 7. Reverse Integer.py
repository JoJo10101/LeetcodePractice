#incoding:utf-8
#num:传入的整数
def change(num):
	num=str(num)
	print num
	if num[0]!='-':
		return num[::-1]
	else:
		box=num[1:]
		return num[0]+box[::-1]

if __name__=="__main__":
	print change(123)
	print change(-123)
	print change(120)
