import numpy as np
numbers = np.random.randint(-1000, 1000, size = np.random.randint(10, 100, size = 1, dtype = int), dtype = int)
print(f"Array length = {len(numbers)}")
print(f"Original array: {numbers}")
l = len(numbers) - 1
for pos in range(len(numbers)):
    j = pos
    for n in range(len(numbers) - pos):
        if numbers[j] > numbers[l - n]:
            j = l - n
    temp = numbers[j]
    numbers[j] = numbers[pos]
    numbers[pos] = temp
print(f"Sorted array: {numbers}")