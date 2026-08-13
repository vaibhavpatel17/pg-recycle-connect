def countt():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    count=0
    number=int(input("enter a number"))
    for i in marks:
        if i>number:
            count+=1
    print(count)
countt()