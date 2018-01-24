#incoding:utf-8
def getlastlen(inputA):
	box=inputA.split(" ")
	return len(box[-1])

def main():
	print getlastlen("Hello World")

if __name__=='__main__':
	main()