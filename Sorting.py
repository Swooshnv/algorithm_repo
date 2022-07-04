import inputnumbers

def validation(inp):
	for i in range(len(inp)):
		if (inp[i] < 0): 
			print('Invalid Input!')
			return 0
		if (len(str(inp[i])) > 5):
			print('Invalid Input!')
			return 0
	return 1

def sort(inp):
	for i in range(len(inp)):
		for j in range(len(inp) - 1):
			if inp[j] < inp[j+1]:
				temp = inp[j+1]
				inp[j+1] = inp[j]
				inp[j] = temp
	return inp

def concat(inp):
	fin = ""
	for i in range(len(inp)):
		fin = fin + str(inp[i])
	return fin


if validation(inputnumbers.A) == 1:
	sorted_array = sort(inputnumbers.A)
	output_to_print = concat(sorted_array)
	print(output_to_print)
