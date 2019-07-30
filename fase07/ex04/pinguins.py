def pinguins(array):
    i = 0
    qtd = len(array)
    while(i < qtd):
        array[i]["roupa"] = {"cabeca": "oculos de sol", "camisa": "jaqueta polar", "pes": "tenis"}
        i = i + 1
    return array