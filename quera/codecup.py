string = 'codecup6'
pos = int(input()) % 8
if pos == 0:
    pos = 8
print(string[pos - 1])
