import math
inp = int(input())
for x in range(inp):
    print(' ' * abs(math.floor(inp / 2) - x) + '*' * (inp - (abs(math.floor(inp / 2) - x) * 2)) + ' ' * abs(math.floor(inp / 2) - x) * 2 + '*' * (inp - (abs(math.floor(inp / 2) - x) * 2)))
