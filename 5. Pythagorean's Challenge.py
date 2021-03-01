t = int(input())

while t>0:
	n = int(input())
	for a in range(n+1):
		aSqare = a*a
		if aSqare>n:
			break
		for b in range(a,n+1):
			bSquare = b*b
			if aSqare+bSquare == n:
				print("({},{})".format(a,b),end=" ")
	print()
	t -= 1