def Smalll():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements:"))
        marks.append(x)
    S=marks[0]
    SS=0
    for i in marks:
        if i<S:
            SS=S
            S=i
        elif i>S and i<SS:
            SS=i

    print(S)
    print(SS)
Smalll()
