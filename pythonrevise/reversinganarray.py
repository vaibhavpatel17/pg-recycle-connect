def reversearray():
    arr=[]
    for i in range(3):
        x=int(input("enter the elements of the array:"))
        arr.append(x)
    n=len(arr)   #we cant have n=x because x is the value we gona enter where as len(arr)give the actucal number of elements
    for i in range(n//2):     #i will be able to get only the first element if i write my print statement outside the loop
        temp=arr[i]
        arr[i]=arr[n-1-i]
        arr[n-1-i]=temp
    print(arr)
reversearray()