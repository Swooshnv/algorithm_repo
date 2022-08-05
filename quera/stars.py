inp = list(map(int, input().split()))
ans = 0
for x in range(inp[0]):
    char = str(input())
    ans += char.count('*')
print(ans)
