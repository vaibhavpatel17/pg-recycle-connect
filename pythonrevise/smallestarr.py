def smallest():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x)
    smallest=marks[0]
    for mark in marks:
        if mark<smallest:
            smallest=mark
    print(smallest)
smallest()