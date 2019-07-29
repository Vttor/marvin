def booleanos(array):
    i = 0
    j = len(array)
    while(i < j):
        if(array[i] == False or array[i] == True):        
            if(str(array[i]) == "False" or str(array[i]) == "True"):
                del array[i]
                j = j - 1
            else:
                i = i + 1
        else:
            i = i + 1
    return array