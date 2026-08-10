def diff():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks of the student:"))
        marks.append(x)   #take values from x for marks
    largest=marks[0]
    smallest=marks[0]
    difference=0
    for i in marks:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
    difference=largest-smallest
    print(difference)
diff()