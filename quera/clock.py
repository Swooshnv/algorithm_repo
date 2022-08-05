time = list(map(int, input().split()))
hour = 12 - time[0]
min = 60 - time[1]
if hour == 12:
    hour = 0
if time[1] == 0:
    min = 0
if hour < 10:
    hour_ = '0' + str(hour)
else:
    hour_ = str(hour)
if min < 10:
    min_ = '0' + str(min)
else:
    min_ = str(min)
print(hour_ + ':' + min_)
