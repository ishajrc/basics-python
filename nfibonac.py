
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
x = int(input("Enter a number: "))
for i in range(1,x):
    print(fib(i)%100)


