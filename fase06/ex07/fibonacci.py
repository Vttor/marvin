def fibonacci(valor):
    a,b,i = 0,1,1
    if(valor == 0):
        return 0
    else:
        while(i<valor):
            a,b,i = b,a+b,i+1
        return b