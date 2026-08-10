def fibonacci():
    n=int(input("enter the number:"))
    a=0
    b=1
    while n>0:
        print(a)
        fib=a+b
        a=b
        b=fib
        n=n-1
       
fibonacci()