def primo(num):
    j = 0
    i = 2
    while(i<num):
        if(num % i == 0):
            j = 1
            i = i + num
        else:
            i = i + 1
    if(j == 1):
        return "Não"
    else:
        return "Sim"