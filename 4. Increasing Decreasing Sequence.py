n = int(input())

a = []
for i in range(n):
	a.append(int(input()))

i = 0
ans = True

while(i<n-1):
	if(a[i+1]<a[i]):
		i += 1
	else:
		break

while(i<n-1):
	if(a[i+1]>a[i]):
		i += 1
	else:
		ans = False
		break

if ans:
	print("true")
else:
	print("false")