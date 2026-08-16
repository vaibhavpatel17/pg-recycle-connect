def repeating():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x) 
    for i in range(len(marks)):
        found=False
        for j in range(len(marks)):
            if i!=j and marks[i]==marks[j]:
                found=True
                break
        if not found:
            print(marks[i])
                
repeating()