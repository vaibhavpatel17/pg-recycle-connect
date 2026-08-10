def smallest():
    n=int(input("enter a number :"))
    small=9
    while n>0:
        digit=n%10
        n=n//10
        if digit<small:
            small=digit
    print(small)

            
smallest()
             
        