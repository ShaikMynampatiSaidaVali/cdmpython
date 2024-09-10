def fib(n):
    if(n<=1):
        return n
    else:
        return(fib(n-1)+fib(n-2))
nterms=int(input("how many terms you need"))
if(nterms<=0):
    print("please enter a positive integer")
else:
    for i in range(nterms):
        print(fib(i))
