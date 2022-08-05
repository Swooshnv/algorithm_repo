out = "Bala Barare"
count = 0
input = int(input())
a = 1
while True:
    count += a
    a += 1
    if out == "Payin Barare":
        out = "Bala Barare"
    else:
        out = "Payin Barare"
    if count >= input:
        break
print(out)
