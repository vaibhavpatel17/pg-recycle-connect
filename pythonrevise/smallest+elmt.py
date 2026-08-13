def smallestt():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the student:"))
        marks.append(x)
    smallest=0
    for i in marks:
            if i>0:
                 smallest=i
                 break     #break is used to stop this loop right here 
    for i in marks:
        if i>0 and i<smallest:
             smallest=i
                 
            
    print(smallest)
smallestt()
