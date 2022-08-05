chess = [1,1,2,2,2,8]
inp = list(map(int, input().split()))
res = [0,0,0,0,0,0]
for x in range(len(chess)):
    res[x] = chess[x] - inp[x]
out = str(res)
out = out.replace(',','')
out = out.replace('[','')
out = out.replace(']','')
print(out)
