def list():
    marks=[10,20,30,40,50]                                #step 1: take one element from marks
    print(marks)
    print(marks[2])
    for i in marks: #prints the value inside the array   #step 2: store it in i
        print(i)                                         #step 3:print i
    print(marks[4])
    for i in range(len(marks)):        #prints the index of the array and len(marks) this returns the number of elements 
        print(i)
list()