inp = list(map(int, input().split()))
count = 0
for x in range(len(inp)):
    if inp[x] >= 80:
        count += 1
if count > 2:
    print('Mamma mia!')
elif count > 0:
    print('Mamma mia!!')
else:
    print('Mamma mia!!!')
