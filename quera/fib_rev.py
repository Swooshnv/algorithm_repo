a = int(input())
b = int(input())
temp = 0
def fib(a, b):
    if b != 1:
        print(a)
        b = b - a
        print(b)
        b = a - b
        a = b - a
        temp = b
        b = a
        a = temp
        fib(a, b)
    else:
        print(1)
fib(a, b)
