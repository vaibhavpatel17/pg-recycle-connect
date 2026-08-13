def largestpsoitive():
        marks=[]
        for i in range(5):
            x=int(input("enter the marks of the student:"))
            marks.append(x)
        largest=0
        for i in marks:
            if i>0 and i>largest:
                largest=i
            if i<=0 and i>largest:
                largest=i
        print(largest)
largestpsoitive()
                
