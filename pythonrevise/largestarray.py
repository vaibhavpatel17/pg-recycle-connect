def largestt():
    marks=[]
    for i in range(5):
        x=int(input("enter the marks:"))
        marks.append(x):   #marks is telling that getthe value of mine from x
    largest=arr[0]
    for i in marks:   #in this for loop i holds the values
        if i>largest:
            largest=i
    print(largest)
largestt()

#if marks[i]>largest:     
 #       largest=marks[i]
 # the above is wrong because marks[i] means the index that means python is trying to extract the value of the 10 index which isnt existing 
 # becuz our list will be [10,20,30]