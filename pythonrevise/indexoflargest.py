def index():
    marks=[]
    for i in range(3):
        x=int(input("enter the marks of the student:"))
        marks.append(x)
    largest=marks[0]
    index_largest=0
    for i in range(len(marks)):
        if marks[i]>largest:   # marks[i] gives the value 
            largest=marks[i]     # i gives the index value
            index_largest=i
    print(largest)
    print(index_largest)
    
index()