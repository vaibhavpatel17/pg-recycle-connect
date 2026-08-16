def difference():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the student:"))
        marks.append(x)
    largest=marks[0]
    smallest=marks[0]
    diff=0
    for i in range(len(marks)):
        if marks[i]>largest:
            largest=marks[i]
        if marks[i]<smallest:
            smallest=marks[i]
    diff=largest-smallest
    print(diff)
difference()

def secondlarg():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the student:"))
        marks.append(x)
    L=marks[0]
    l=[]
    for i in range(len(marks)):
        if marks[i]>L:
            l=L
            l=
            
