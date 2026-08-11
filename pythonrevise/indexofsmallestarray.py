def smallest():
    arr=[]
    for i in range(3):
        x=int(input("enter the array elements:"))
        arr.append(x)
    small=arr[0]
    smallest_index=0
    for i in range (len(arr)):
        if arr[i]<small:
            small=arr[i]
            smallest_index=i
    print(small)
    print(smallest_index)
smallest()