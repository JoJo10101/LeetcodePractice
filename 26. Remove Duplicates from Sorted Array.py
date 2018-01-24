#incoding:utf-8
#set()#set函数去重，但是返回会显示set
def clear(nums):
	d={}
	for i in nums:
		if i in d.keys():
			continue
		else:
			d[i]=nums.count(i)

	for i in nums:
		if d[i]==1:
			continue
		for j in range(d[i]-1):
			nums.remove(i)
	return nums

if __name__=='__main__':
	print clear([1,2,4])
	print clear([1,1,2,4])