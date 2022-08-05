import math
count = list(map(int, input().split()))
jars = list(map(int, input().split()))
jams = 0
for x in range(count[0]):
    jams += jars[x]
print(count[0] - int(math.ceil(float(jams) / float(count[1]))))
