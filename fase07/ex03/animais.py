def animais(array):
    x = len(array)
    i = 0
    idade = 5
    while(i < x):
        del(array[i]["altura"])
        array[i]["idade"] = idade
        i = i + 1
        idade = idade + 1
    return array