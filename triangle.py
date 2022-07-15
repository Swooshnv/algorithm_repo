import math

#initialize variables
output = 0

def count(H):
    times = 0
    for x in range(H):
        calc = math.sqrt((H*H)-(x*x))   #calculate the other side
        if calc.is_integer() == 1 and x != 0:   #check if both sides are integer
            times = times + 1
    return int(times/2)  #because variants are counted twice

for x in range(T):
    #print("Enter the Hypotenuse: ")
    output = count(n)    #desired input of Hypotenuse
    print(output)
