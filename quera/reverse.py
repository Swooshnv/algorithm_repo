count = int(input())
sentence = list(map(str, input().split()))
out = ""
for x in range(count):
    out = out + sentence[count - 1 - x] + ' '
print(out)
