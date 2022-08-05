inp = str(input())
rev = ''
for x in range(len(inp)):
    rev += inp[len(inp) - 1 - x]
if inp == rev:
    print('YES')
else:
    print('NO')

