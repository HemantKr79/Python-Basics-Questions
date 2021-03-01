cumulative_sum = 0

while(True):
	num = int(input())
	cumulative_sum += num
	if cumulative_sum>=0 :
		print(num)
	else:
		break