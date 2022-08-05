a = str(input())
b = str(input())
rev_a = ''
rev_b = ''
for x in range(len(a)):
    rev_a += a[len(a) - 1 - x]
    rev_b += b[len(b) - 1 - x]
if int(rev_a) > int(rev_b):
    print(b + ' < ' + a)
elif int(rev_b) > int(rev_a):
    print(a + ' < ' + b)
else:
    print(a + ' = ' + b)
