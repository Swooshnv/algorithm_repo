char = str(input())
res = 0
while True:
    res = 0
    if int(char) < 10:
        break
    else:
        for x in range(len(char)):
            res += int(char[x])
        char = str(res)
print(char)
