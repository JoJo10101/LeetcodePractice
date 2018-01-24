#incoding:utf-8
def clear(nums,val):

	for i in range(nums.count(val)):
		nums.remove(val)
	return nums

if __name__=='__main__':
	print clear([1,1,2,4],1)
	print clear([1,1,2,4],4)
	print clear([1,1,2,4],0)
