def frequency():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements in an array:"))
        marks.append(x)
    m=int(input("enter the element to search:"))    
    f=0
    for i in marks:
        t=i
        if t==m:
            f+=1
        else:
            print("no element found")
    print(f)
frequency()