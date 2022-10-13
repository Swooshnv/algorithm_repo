import numpy as np
numbers = np.random.randint(-1000, 1000, size = np.random.randint(10, 100, size = 1, dtype = int), dtype = int)

def merge(numbers, a, b, c):
    i = a
    j = b + 1
    k = a
    numbers_2 = numbers
    while (i <= q) and (j <= c):
        if numbers[i] < numbers[j]:
            numbers_2[k] = numbers[i]
            i =+ 1
        else:
            numbers_2[k] = numbers[j]
            j =+ 1
        k =+ 1
    while (i <= b):
        numbers_2[k] = numbers[i]
        k =+ 1
        i =+ 1
    while (j <= c):
        numbers_2[k] = numbers[i]
        k =+ 1
        j =+ 1
    for loop in range(c - a):
        numbers[loop + a] = numbers_2[loop + a]
    return numbers

def mergesort(numbers, a, c):
    if (a < c):
        b = (a + c) / 2
        mergesort(numbers, a, b)
        mergesort(numbers, b + 1, c)
        merge(numbers, a, b, c)
