inp = int(input())
lst = list(map(int, input().split()))
for x in range(inp):
    if lst[x] > 3:
        print('*')
    else:
        print('*' * lst[x])
