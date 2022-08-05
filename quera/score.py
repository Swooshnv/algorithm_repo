score = int(input())
days = int(input())
if days == 7:
    print(score)
elif days == 0:
    print(20)
else:
    score = score - days
    if score < 0:
        score = 0
    print(score)
