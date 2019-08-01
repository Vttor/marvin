
def precoMedio(*x):
    arr = []
    qtd = len(x)
    soma = 0
    for i in range(0,qtd):
        soma = soma + float(x[i]["preco"])
        arr.insert(i,str(x[i]["preco"]) + str(i))
    arr.sort()
    print("O produto mais caro se chama " + x[arr[qtd - 1][-1:]]["preco"])
    
print(precoMedio({"nome": "Batata", "preco": 2.20},{"nome": "Melancia", "preco": 4.92}))