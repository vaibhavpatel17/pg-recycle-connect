def palindrome():
    n=int(input("enter a number:"))
    P=0
    PP=n
    while n>0:
        digit=n%10
        P=P*10+digit
        n=n//10
    if P==PP:
        print("palindrome")
    else:
        print("not a palindrome")
palindrome()