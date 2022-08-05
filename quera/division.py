inp = int(input())
sum = 0
for x in range(inp):
    if inp % (x + 1) == 0 and x + 1 != inp:
        sum += (x + 1)
if sum == inp:
    print("YES")
else:
    print("NO")
