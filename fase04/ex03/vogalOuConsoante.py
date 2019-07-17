def vogalOuConsoante(letra):
    letra = letra.lower()
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return "Vogal"
    else:
        return "Consoante"