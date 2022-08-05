inp = list(map(str, input().split()))
key = inp[1]
for x in range(int(inp[0])):
    pos = list(map(str, input().split()))
    if pos[0] == key:
        key = pos[1]
    elif pos[1] == key:
        key = pos[0]
print(key)
