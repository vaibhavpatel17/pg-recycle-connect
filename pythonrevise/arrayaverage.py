def avarage():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the student:"))
        marks.append(x)
    sum=0
    avg=0
    count=0
    for i in marks:
        if i>0:
            count+=1
            sum=sum+i
    avg=sum/count      #"//" gives floor diving that is only quotient or round off number BUT "/" gives the qotient in decimal form 

    print(avg)
avarage()
