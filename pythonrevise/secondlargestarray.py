def secondlargest():
    marks=[]
    for i in range(5):
            x=int(input("enter the marks:"))
            marks.append(x)
    largest=marks[0]
    large=0
    for i in marks:
            if i>largest:
                large=largest
                largest=i
            if i<largest and i>large:
                  large=i
    print(largest)
    print(large)
secondlargest()