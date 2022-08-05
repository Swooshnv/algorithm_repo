inp = int(input())
sum = ''
a = 1
for x in range(inp):
    sum += str(a)
    a += 1
print(str(sum)[inp - 1])
