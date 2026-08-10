def largest():
    n=int(input("enter a number "))
    large=1
    smallest=9
    while n>0:
        digit=n%10
        n=n//10
        if digit>large:
            large=digit
        if digit<smallest:
            smallest=digit
    diff=large-smallest
    print(diff)
    print(large)
    print(smallest)
largest()