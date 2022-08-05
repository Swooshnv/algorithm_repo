inp = int(input())
names = list(map(str, input().split()))
for x in range(inp):
    for y in range(x):
        if y < x:
            print(names[x] + ': salam ' + names[x - y - 1] + '!')
for x in range(inp):
    for y in range(inp - x):
        if y == 0:
            print(names[x] + ': khodafez bacheha!')
        else:
            print(names[x + y] + ': khodafez ' + names[x] + '!')

