def somaPares(num1,num2):
    i = round(num1,0)
    soma = 0
    while(i <= num2):
        if(i % 2 == 0):
            soma = soma + i
            i = i + 1
        else:
            i = i + 1
    if(round(num1,0) == num1 or round(num1,0) % 2 != 0):
        return soma
    else:
        return soma - round(num1,0)