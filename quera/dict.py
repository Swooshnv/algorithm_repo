ans = ''
for x in range(5):
    inp = str(input())
    if inp.count('MOLANA') > 0 or inp.count('HAFEZ') > 0:
        ans = ans + str(x + 1) + ' '
print(ans)
