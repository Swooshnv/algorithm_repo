import math
inp = list(map(float, input().split()))
ans = inp[0]
for x in range(int(inp[1])):
    ans = ans / 2
print(int(math.floor(ans)))
