def summ():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    sum=0
    number=int(input("enter the number to search:"))
    for i in marks:
        if i>number:
            sum=sum+i
    print(sum)
summ()
