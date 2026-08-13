def elements():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements:"))
        marks.append(x)
    count=0
    lower=int(input("enter the lower limit:"))
    upper=int(input("enter the upper limit:"))
    for i in marks:
        if i>=lower and i<=upper:
            count+=1
    print(count)
elements()