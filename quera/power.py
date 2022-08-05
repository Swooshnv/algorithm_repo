a = 2  
b = int(input())
count = 1
while True:
    if a > b:
        break
    a = 2 ** (1 + count)
    count += 1
print(a)
