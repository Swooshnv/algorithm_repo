inp = list(map(str, input().split()))
out = ""
for x in range(int(inp[0])):
    out += 'copy of '
out += inp[1]
print(out)
