def sum():
    n=int(input("enter the number:"))
    digit=0
    g=0
    while n>0:
        digit=n%10
        g=g+digit
        n=n//10
    print(g)   
sum()
