import math
import statistics as stc

T = list(map(int, input().split()))
S = []
val = []
total = T[1]
median = 0
days = 1000000000
fin_int = 0
fin_str = 0
for x in range(T[0]):
    temp = list(map(int, input().split()))
    if temp[0] != 0:
        value = temp[1] / temp[0]
    else:
        value = 10000000
    S.append(temp)
    val.append(value)

total = T[1]
median = stc.median(val)
for x in range(T[0]):
    if val[x] <= median:
        fin_int = fin_int + S[x][0]
        fin_str = fin_str + S[x][1]
fin_str = fin_str + T[1]
days = math.ceil(fin_str/fin_int)
print(days)
