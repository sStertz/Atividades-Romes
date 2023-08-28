def apagar_vogal():
    texto = input("Insira um texto: ")
    return texto.lower().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")

print(apagar_vogal())
