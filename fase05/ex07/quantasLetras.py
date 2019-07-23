def quantasLetras(array):
    qtd = len(array)
    controle = 0
    soma = 0
    while(controle < qtd):
        soma = soma + len(array[controle])
        controle = controle + 1
    return soma