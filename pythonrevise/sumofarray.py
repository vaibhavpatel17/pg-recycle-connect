def summ():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of student"))
        marks.append(x)

    sum=0   #try using total instead of sum becuz sum() is an inbuilt function 
    for mark in marks:
        sum=sum+mark

    print(sum)
summ()
