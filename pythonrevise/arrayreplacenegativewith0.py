def replace():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of te student:"))
        marks.append(x)
    neg=0
    for i in range(len(marks)):
        if marks[i]<0:
            marks[i]=0
    print(marks)
replace()
            