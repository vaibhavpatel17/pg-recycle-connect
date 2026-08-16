def countdupelements():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    count=0
    arr=[]
    for i in range(len(marks)):
        for j in range(i):
            if marks[i]==marks[j]:
                if marks[i] not in arr:
                    arr.append(marks[i])
                    count+=1
    print(count)
                
countdupelements()