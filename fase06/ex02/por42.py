def por42(num1,num2):
    i = 0
    j = 0
    while(i == 0):
        if (num1%42 != 0 and j != 2):
            num1 = num1 + 1
        else:
            j = j + 1
            if (j != 2):
                num1 = num1 + 1
        if (j == 2):
            i = 1
        if(num1 > num2):
            num1 = False
            i = 1
            print("Não encontrado")
    return num1