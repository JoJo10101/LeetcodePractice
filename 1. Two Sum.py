#incoding:utf-8
#t:为目标数
#nums:为传入的数组
def findsum(t,nums):
	numslen=len(nums)
	
	#print numslen
	for i in range(numslen):
		for j in range(i,numslen):
			if int(nums[i])+int(nums[j])==int(t):
				print i,j

if __name__=="__main__":
	findsum(2,[1,1,0,2])
