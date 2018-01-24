#incoding:utf-8
def isvalid(strs):
	box=[]
	if len(strs)<2:
		return False
	else:
		if len(strs)%2!=0:
			return False
		elif strs[0] in (')',']','}'):
			return False
		elif strs[-1] in ('(','[','{'):
			return False

		for i in strs:
			if i in ('(','[','{'):
				box.append(i)
			if i ==')' and box[-1]=='(':
				box.pop()
			if i ==']' and box[-1]=='[':
				box.pop()
			if i =='}' and box[-1]=='{':
				box.pop()
		if box==[]:
			return True
		else:
			return False

if __name__=='__main__':
	print isvalid('')
	print isvalid('(]]')
	print isvalid(')[')
	print isvalid('([')
	print isvalid('([]{})')
	print isvalid('(]')