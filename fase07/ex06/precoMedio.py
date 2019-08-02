def precoMedio(*x):
    qtd = len(x)
    arr = []
    soma = 0
    for i in range(0,qtd):
        arr.insert(i,x[i]["preco"])
        soma += x[i]["preco"]
    arr.sort()
    maiorPreco = arr[qtd - 1]
    for i in range(0,qtd):
        if (x[i]["preco"] ==  maiorPreco):
            print("O produto mais caro se chama \"" + x[i]["nome"] + "\"")
            break
    return round(soma/qtd,2)