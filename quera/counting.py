inp = str(input())
char = ""
for x in range(len(inp)):
    char = ""
    char = char + inp[x] + ": " + (inp[x] * int(inp[x]))
    print(char)
