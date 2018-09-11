try:
	m,n=map(int,raw_input().split())
	for i in range(m+1,n):
		if(i%2!=0):
			continue
		print(i),
except:
	print('invalid')
	
