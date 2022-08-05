a = list(map(int, input().split()))
if a.count(0) > 0:
    print('No')
elif a[0] + a[1] + a[2] == 180:
    print('Yes')
else:
    print('No')
