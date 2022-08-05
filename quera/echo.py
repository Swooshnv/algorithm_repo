inp = str(input())
for x in range(len(inp)):
    print((inp[x] * (x + 1)) + inp[(x + 1):])
