import math
inp = float(input())
floor = int(math.floor(inp / 2)) + 1
ceil = int(math.ceil(inp / 2)) + 1
print(ceil * floor)
