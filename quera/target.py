pos = list(map(int, input().split()))
length = int(input())
hit = list(map(int, input().split()))
if (hit[0] >= pos[0] and hit[0] <= (pos[0] + length)) and (hit[1] <= pos[1] and hit[1] >= (pos[1] - length)):
    print('Mahdi')
else:
    print('Parsa')
