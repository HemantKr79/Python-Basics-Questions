n = int(input())

for i in range(n,0,-1):
	for j in range(1,i+1):
		print(j,end=" ")
	for k in range(2*(n-i) - 1):
		print("*",end=" ")
	print()