n = int(input('Enter the number of kids'))

candies = []
for i in range(n):
    x = input('enter the number of candies')
    candies.append(x)
print(candies)

extraCandies = input('enter the amount of extra candies')
out = []
for i in range(len(candies)) :
    if int(candies[i]) + int(extraCandies) >= int(max(candies)) :
        y = 'true'
        out.append(y)
    else:
        y = 'false'
        out.append(y)
print(out)