inp = str(input())
F = inp.count('F')
if inp.count('F') == 0:
    F = 0
L = inp.count('L')
if inp.count('L') == 0:
    L = 0
D = inp.count('D')
if inp.count('D') == 0:
    D = 0
T = inp.count('T')
if inp.count('T') == 0:
    T = 0
print(2 ** (F + L + D + T))
