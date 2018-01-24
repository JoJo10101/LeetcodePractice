#incoding:utf-8
def findIndex(strA,target):
	if target<=strA[0]:
		return 0
	if target>strA[-1]:
		return len(strA)

	i=0
	while i<len(strA):
		if target>strA[i]:
			i=i+1
		else:
			return i

if __name__=='__main__':
	print findIndex([1,3,5,6,7],0)
	print findIndex([1,3,5,6,7],1)
	print findIndex([1,3,5,6,7],2)
	print findIndex([1,3,5,6,7],4)
	print findIndex([1,3,5,6,7],5)
	print findIndex([1,3,5,6,7],8)
	print findIndex([1,3,5,6,7],7)
	

