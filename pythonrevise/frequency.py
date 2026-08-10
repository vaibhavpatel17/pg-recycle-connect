def frequency():
    n=int(input("enter the number:"))
    f=int(input("enter the digit to search:"))
    freq=0
    while n>0:
        digit=n%10
        n=n//10
        if digit==f:
            freq+=1
    print(freq)
frequency()


    