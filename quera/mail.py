inp = str(input())
for x in range(len(inp)):
    if inp.count(inp[x]) % 2 != 0:
        out = 'bad'
        break
    else:
        out = 'khoob'
print(out)
