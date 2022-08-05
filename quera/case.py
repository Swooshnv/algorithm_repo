inp = int(input())
char = ''
CAPS = 0
for x in range(inp):
    string = str(input())
    if string == 'CAPS':
        if CAPS == 0:
            CAPS = 1
        else:
            CAPS = 0
        continue
    elif CAPS == 0:
        char += string
    else:
        char += string.upper()
print(char)
