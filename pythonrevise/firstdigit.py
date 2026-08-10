def firstdigit():
    n=int(input("enter the number:"))
    while n>0:
        digit=n%10
        n=n//10
    print(digit)
firstdigit()