a = []
for x in range(3):
    a.append(input())
max_num = max(a)
res = 0
for x in range(len(a)):
    if max_num != a[x]:
        res += int(a[x]) ** 2
if res == int(max_num) ** 2 and a.count(int(max_num)) == 1:
    print("YES")
else:
    print("NO")
