def countodd():
    n=int(input("enter the number:"))
    count=0
    sum=0
    while n>0:
        digit=n%10
        n=n//10
        if digit%2!=0:
            count+=1
            sum=sum+digit      #we have to add digit to the sum , not count , count is just a variable to count number od odd or even digits in a number
    print(count)
    print(sum)
countodd()