inp = []
for x in range(4):
    inp.append(float(input()))
sum = 0.0
ave = 0.0
prod = 1.0
mx = "{:.6f}".format(max(inp))
mn = "{:.6f}".format(min(inp))
for x in range(4):
    sum += inp[x]
    ave += (inp[x] / 4)
    prod = prod * inp[x]
sum = "{:.6f}".format(sum)
ave = "{:.6f}".format(ave)
prod = "{:.6f}".format(prod)
print('Sum : ' + str(sum))
print('Average : ' + str(ave))
print('Product : ' + str(prod))
print('MAX : ' + str(mx))
print('MIN : ' + str(mn))
