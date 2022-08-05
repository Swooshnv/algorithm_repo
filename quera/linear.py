import numpy as np

a = list(map(int, input().split()))
if a[0] != 0:
    b = float(a[1]) / float(a[0])
else:
    b = "infinite"
if b == 0.0:
    b = "invalid"
else:
    b = "unique"
print(b)
