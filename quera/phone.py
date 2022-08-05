count = int(input())
for x in range(count):
    temp = str(input())
    rev = ''
    cons = ''
    done = 0
    if temp[0] == '0':
        print('Rond Nist')
        continue
    for x in range(len(temp)):
        rev =+ temp[len(temp) - 1 - x]
        if cons != temp[x]:
            cons = temp[x]
        elif cons == temp[x]:
            cons += temp[x]
        if len(cons) == 3:
            print('Ronde')
            done = 1
            break
    if rev == temp and done != 1:
        print('Ronde!')
        done = 1
        continue
    for x in range(10):
        if temp.count(str(x)) > 3 and done != 1:
            print('Ronde!')
            done = 1
            break
    if done != 1:
        print('Rond Nist')
