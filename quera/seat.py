inp = list(map(int, input().split()))
char = ''
a = 0
if inp[1] > 10:
    a = 21 - inp[1]
    char = "Left "
else:
    a = inp[1]
    char = "Right "
out = ""
out = out + char + str(11 - inp[0]) + " " + str(a)
print(out)
