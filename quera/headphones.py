a = list(map(str, input().split()))
b = list(map(str, input().split()))
if a[0] == b[1] or a[1] == b[0] or a[0] == a[1] or b[0] == b[1]:
    print('YES')
else:
    print('NO')
