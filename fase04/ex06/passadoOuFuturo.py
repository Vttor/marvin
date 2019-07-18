def passadoOuFuturo(tempo):
    if int(tempo/1000) < 1445385600:
        return "Passado"
    else:
        return "Futuro"