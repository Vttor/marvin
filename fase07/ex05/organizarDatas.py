def organizarDatas(array):
    qtd = len(array)
    for i in range(0,qtd):
        array[i]["id"] = int(array[i]["dataDeChegada"][6:] +array[i]["dataDeChegada"][:-8]+ array[i]["dataDeChegada"][3:5])
    array = sorted(array, key = lambda k: k["id"])
    for i in range(0,qtd):
        del(array[i]["id"])
    return array