import numpy as np
S = np.random.randint(0, 150, size = np.random.randint(5, 15, size = 1, dtype = 'int64'))

def partition(S, low, high):
    if(low < high):
        count = high - low + 1
        pivot = S[low]
        j = low
        for i in range(count - 1):
            if (S[i + low + 1] < pivot):     
                j += 1
                temp = S[j]
                S[j] = S[i + low + 1]
                S[i + low + 1] = temp
                print(S)
        temp = S[j]
        S[j] = S[low]
        S[low] = temp
        return j

def quickSort(S, low, high):
    if (low < high):
        pivot = partition(S, low, high)
        quickSort(S, low, pivot - 1)
        quickSort(S, pivot + 1, high)
print(f"Entry List: {S}")
quickSort(S, 0, len(S) - 1)
print(f"Sorted List: {S}")
