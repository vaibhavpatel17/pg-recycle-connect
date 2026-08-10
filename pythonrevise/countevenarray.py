def evenarray():
    marks=[]    
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    count=0
    for mark in marks:   #here "marks" is just a variable we can use any name 
        if mark%2==0:
            count+=1
    print(count)
evenarray()