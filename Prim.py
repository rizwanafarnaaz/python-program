number=int(raw_input())
for x in range(2, number):
	if number%x == 0:
		print('no')
	break
else:
	print('yes')
