def entreNumeros(x,y):    
    def acabar(mi,ma):
        while(mi <= ma):
            print (mi)
            mi = mi + 1
    if (x<y):
        acabar(x,y)
    else:
        acabar(y,x)