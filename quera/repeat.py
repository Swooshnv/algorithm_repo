inp = 1
a = []
while True:
    inp = int(input())
    if inp == 0:
        break
    a.append(inp)
for x in range(len(a)):
    print(a[len(a) - x - 1])
