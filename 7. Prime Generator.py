N = 10000000
primes = []
isPrime = [True]*N

def seive():
	for i in range(4,N,2):
		isPrime[i] = False
	primes.append(2)
	for i in range(3,N,2):
		if isPrime[i] == True:
			primes.append(i)
			for j in range(i*i,N,i):
				isPrime[j] = False

t = int(input())
seive()

while t>0:
	str_input = input().split()
	m,n = int(str_input[0]),int(str_input[1])
	nums = [True]*(n-m+1)
	for x in primes:
		if x*x > n:
			break
		start = (m//x)*x
		if x>=m and x<=n:
			start = x*2
		while start < m:
			start += x
		while start <= n:
			nums[start-m] = False
			start += x
	for i in range (n-m+1):
		if nums[i] and (i+m)!=1:
			print(i+m,end=" ")
	print()
	t -= 1