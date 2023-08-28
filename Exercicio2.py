def quantidade_caracteres():
    palavra = input("Insira um texto:")
    return len(palavra)

print("Essa palavra tem " + str(quantidade_caracteres()) + " caractéres.")