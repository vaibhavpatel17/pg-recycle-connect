def counteven():
    n=int(input("enter the nmber of digits"))
    count=0
    sum=0
    while n>0:
        digit=n%10
        n=n//10
        if digit %2==0:
            count+=1
            sum=sum+digit
    print(count)
    print(sum)
counteven()