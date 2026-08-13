def positive():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the students:"))
        marks.append(x)
    total=0
    for i in marks:
        if i>0:
            
            total+=i

    print(total)
positive()