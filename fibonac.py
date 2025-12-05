x=int(input("Enter a number: "))
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(x):
    print(fib(i))
