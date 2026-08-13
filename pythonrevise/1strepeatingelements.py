def rep():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements:"))
        marks.append(x)
    arr=0
    for i in marks:
        marks[arr]=i
        arr+=1
    if marks[arr]==i:

