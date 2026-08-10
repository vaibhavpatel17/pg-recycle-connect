def secondlargest():
    n=int(input("enter the number:"))
    largest=1
    secondlarge=0
    while n>0:
        digit=n%10
        n=n//10
        if digit>largest:
            secondlarge=largest
            largest=digit
        if digit<largest and digit>secondlarge:
            secondlarge=digit
        
    print(secondlarge)
    print(largest)
secondlargest()
