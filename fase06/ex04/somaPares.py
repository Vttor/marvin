def somaPares(num1,num2):
    def acabar(num1,num2):
        from math import floor
        i = floor(num1)
        soma = 0
        while(i <= num2):
            if(i % 2 == 0):
                soma = soma + i
                i = i + 1
            else:
                i = i + 1
        if(floor(num1) == num1 or floor(num1) % 2 != 0):
            return (soma)
        else:
            return soma - floor(num1)
    if(num1<num2):
        return acabar(num1,num2)
    else:
        return acabar(num2,num1)