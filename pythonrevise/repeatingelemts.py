def repeat():
    marks=[]
    for i in range(5):
        x=int(input("enter the elements:"))
        marks.append(x)
    arr=[]    #this is the empty array to store the numbers
    for i in marks:
        if i not in arr:
            arr.append(i)
    print(arr)
    print(i)   #first repeated element
repeat()