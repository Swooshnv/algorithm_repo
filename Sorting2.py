import numpy as np
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
			lock=0
			for x in range(len(str(inp[j + 1]))):
				if x > len(str(inp[j])) & lock == 0:
					if int(str(inp[j + 1])[x]) >= int(str(inp[j])[x - 1]):
						temp = inp[j + 1]
						inp[j + 1] = inp[j]
						inp[j] = temp
						lock=1
						break
					break
				if x <= len(str(inp[j])) & lock == 0:	
					if int(str(inp[j + 1])[x]) > int(str(inp[j])[x]):
						temp = inp[j + 1]
						inp[j + 1] = inp[j]
						inp[j] = temp
						lock=1
						break

	return inp

def concat(inp):
	fin = ""
	for i in range(len(inp)):
		fin = fin + str(inp[i])
	return fin


num = np.array(inputnumbers.A)
if validation(num) == 1:
	sorted_array = sort(inputnumbers.A)
	output_to_print = concat(sorted_array)
	print(output_to_print)
