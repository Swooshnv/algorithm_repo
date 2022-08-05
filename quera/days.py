a = int(input())
char = str(input())
a += int(input())
char += str(input())
a += int(input())
char += str(input())
days = 7
if char.count('jome') > 0:
    days = days - 1
    a = a - char.count('jome')
if char.count('1') > 0:
    days = days - 1
    a = a - char,count('1')
if char.count('2') > 0:
    days = days - 1
    a = a - char.count('2')
if char.count('3') > 0:
    days = days - 1
    a = a - char.count('3')
if char.count('4') > 0:
    days = days - 1
    a = a - char.count('5')
if char.count('5') > 0:
    days = days - 1
    a = a - 1
if a > 0:
    days = days - 1
print(days)

