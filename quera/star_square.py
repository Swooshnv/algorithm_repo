count = int(input())
for x in range(count):
    if x == 0 or x == (count - 1):
        print('*' * count)
    else:
        print('*' + ' ' * (count - 2) + '*')
