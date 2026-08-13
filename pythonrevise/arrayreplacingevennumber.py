def replaceeven():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    for i in range(len(marks)):
        if marks[i]%2==0:
            marks[i]=0
    print(marks)
replaceeven()