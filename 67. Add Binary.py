#incoding:utf-8
def addBin(a,b):
	return bin(int(a,2)+int(b,2))

def main():
	print addBin('11','1')
	
if __name__=='__main__':
	main()