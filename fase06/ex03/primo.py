def primo(num):
    from math import floor
    from math import ceil
    num = abs(num)
    if(floor(num) != num):
        return "Não"
    else:
        j = 0
        i = 2
        x = 0
        while(i<ceil(num/2)):
            if(num % i == 0):
                j = 1
                i = i + num
            else:
                i = i + 1
        if(j == 1 or num == 1 or num == 0):
            return "Não"
        else:
            return "Sim"