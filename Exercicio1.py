def substituir_vogal():    
    texto = input("Insira um texto:")
    return texto.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
    
print(substituir_vogal())