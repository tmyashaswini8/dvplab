def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return (fib(n-1)+fib(n-2))

num=int(input("Enter a number"))
if(num>=0):
    f=fib(num)
    print("fib sequence is",f)
else:
    print("It is not a valid number")