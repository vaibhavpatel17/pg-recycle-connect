def zero():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of thestudent:"))
        marks.append(x)
    position=0
    for i in range(len(marks)):
        if marks[i]!=0:
            marks[position]=marks[i]    #to bring the non-zero digits to the front
            position+=1
    while position<len(marks):          #while loop is outside the for loop cause its main objective is to just find the non zero digits 
        marks[position]=0
        position+=1
    print(marks)
zero()