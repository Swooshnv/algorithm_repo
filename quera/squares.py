a = int(input())
b = int(input())
string = ''
if (a - b) % 2 != 0:
    print('Wrong difference!')
elif b >= a:
    print('Wrong order!')
else:
    for x in range(a):
        string = ''
        for y in range(a):
            if y > (((a - b) / 2) - 1) and y < ((a + b) / 2) and x > (((a - b) / 2) -1) and x < ((a + b) / 2):
                string += '  '
            else:
                string = string + '* '
        print(string)
