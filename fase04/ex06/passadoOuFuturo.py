def passadoOuFuturo(tempo):
    if tempo/1000 < 1445385600:
        return "Passado"
    else:
        return "Futuro"