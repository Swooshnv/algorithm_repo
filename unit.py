T = int(input())
temp = list(map(int, input().split()))
calc = 0
a = 1
ptr = 0
for x in range(T):
    ptr = temp[x]
    if temp.count(ptr) == 1 and a == 1:
        a = 0
        calc = temp[x]
        continue
    if temp.count(ptr) == 1:
        calc = calc ^ temp[x]

print(calc)
