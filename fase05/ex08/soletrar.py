def soletrar(pal):
    array = []
    ctr = 0
    qtd = len(pal)
    while (ctr < qtd):
        array.insert(ctr,pal[ctr])
        ctr = ctr + 1
    return array