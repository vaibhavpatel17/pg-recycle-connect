def odd():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the student:"))
        marks.append(x)
    count=0
    sum=0
    for i in marks:
        if i%2!=0:
            count+=1
            print(i)
            sum=sum+i
    
    print(count)
    print(sum)  
odd()