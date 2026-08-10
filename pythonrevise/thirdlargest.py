def thirdlargest():
    n=int(input("enter the number:"))
    largest=0
    large=0
    l=0
    while n>0:
        digit=n%10
        n=n//10
        if digit>largest:
            l=large
            large=largest
            largest=digit

        if digit<largest and digit>large and digit>l :
            l=large
            large=digit
        if digit<largest and digit<large and digit>l:
            l=digit
            
    print(l)
thirdlargest()