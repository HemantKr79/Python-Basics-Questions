def generate(index,n_open,n_close,n,my_string):
	if index==2*n:
		print(my_string)
		return
	if n_close<n_open:
		my_string += ')'
		generate(index+1,n_open,n_close+1,n,my_string)
		my_string = my_string[:-1]
	if n_open < n:
		my_string += '('
		generate(index+1,n_open+1,n_close,n,my_string)
		my_string = my_string[:-1]
		
n = int(input())
generate(0,0,0,n,'')
