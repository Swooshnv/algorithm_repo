import numpy as np
numbers = np.random.randint(-1000, 1000, size = np.random.randint(10, 100, size = 1, dtype = int), dtype = int)
print(f"Array length = {len(numbers)}")
print(f"Original array: {numbers}")
for pos in range(len(numbers) - 1):
    for n in range(pos):
        if numbers[pos - n + 1] > numbers[pos - n]:
            temp = numbers[pos - n + 1]
            numbers[pos - n + 1] = numbers[pos - n]
            numbers[pos - n] = temp
print(f"Sorted array: {numbers}")