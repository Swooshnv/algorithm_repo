count = int(input())
cor = str(input())
ans = str(input())
ans_count = 0
for x in range(count):
    if ans[x] != cor[x]:
        ans_count += 1
print(ans_count)
