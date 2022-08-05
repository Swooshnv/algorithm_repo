a = int(input())
char = ""
for x in range(a):
    char = ""
    for y in range(a):
        char = char + str((x + 1) * (y + 1)) + " "
    print(char)
