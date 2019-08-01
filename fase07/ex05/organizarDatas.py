def organizarDatas(array):
    qtd = len(array)
    arr = []
    for i in range(0,qtd):
        array[i]["id"] = i
        arr.insert(i, array[i]["dataDeChegada"][6:] +array[i]["dataDeChegada"][:-8]+ array[i]["dataDeChegada"][3:5])
    print(array)    
    print(arr)
organizarDatas([{"planeta": "Plutão", "dataDeChegada": "02/21/2085"}, {"planeta": "Mercurio", "dataDeChegada": "05/13/2098"}])