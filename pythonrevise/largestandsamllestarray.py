def largestandsmallest():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    smallest=marks[0]
    largest=marks[0]
    for i in marks:
        if i<smallest:
            smallest=i
        if i>largest:
            largest=i
    print(largest)
    print(smallest)
largestandsmallest()