def countt():
    marks=[]
    for i in range(5):
        x=int(input("enter the mraks of the student:"))
        marks.append(x)
    count_positive=0
    count_negative=0
    count_zero=0
    for i in marks:    #TRAVERSING
        if i>0:                   #CLASSIFYING EACH ELEMENT
            count_positive+=1
        if i<0:                   #CLASSIFYING EACH ELEMENT
            count_negative+=1
        if i==0:                  #CLASSIFYING EACH ELEMENT
            count_zero+=1         #UPDATING EACH ELEMENT
    print(count_positive)
    print(count_negative)
    print(count_zero)
countt()
        