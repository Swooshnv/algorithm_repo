count = int(input())
states = 0
state = int(input())
for x in range(count - 1):
    temp = int(input())
    if state != temp:
        states += 1
        state = temp
print(states)
