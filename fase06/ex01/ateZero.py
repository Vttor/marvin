def ateZero(num):
    array = []
    i=0
    if(num<0):
        while(num<=0):
            array.insert(i,num)
            num = num + 1
            i = i + 1
    else:
        while(i<=num):
            array.insert(i,i)
            i = i + 1
    return array