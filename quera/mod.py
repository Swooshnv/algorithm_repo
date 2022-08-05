inp = list(map(int, input().split()))
dist = inp[0]
one = 0
two = 0
while True:
    if dist % inp[1] != 0:
        two += 1
        dist = dist - inp[2]
    if dist % inp[1] == 0:
        one = dist / inp[1]
        break
    if dist < 0:
        one = -1
        break
if one != -1:
    print(str(int(one)) + ' ' + str(int(two)))
else:
    print(-1)
