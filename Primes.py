a=int(raw_input())
def prime(x):
	for i in range(2,x):
		if(x%i<>0):
			return("yes")
		else:
			return("no")
c=prime(a)
print(c)
