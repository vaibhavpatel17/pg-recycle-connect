def rep():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements:"))
        marks.append(x)
    found=False                  #this is called as flag
    for i in range(len(marks)):  #this is the outer loop , it chooses the current element
        for j in range(i):       #this is the inner loop which looks for a match 
            if marks[i]==marks[j]:
                print(marks[i])
                found=True
                break
        if  found:          #this is used to break or stpop the inner loop 
            break
rep()

