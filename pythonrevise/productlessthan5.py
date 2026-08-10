def product():
    n=int(input("enter the number:"))
    count=0
    product=1
    while n>0:
        digit=n%10
        n=n//10
        if digit<5:
            count+=1
            product=product*digit
    print(product)
product()