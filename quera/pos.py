pos = list(map(int, input().split()))
if pos[1] == pos[3]:
    print("Horizontal")
elif pos[0] == pos[2]:
    print("Vertical")
else:
    print("Try again")
