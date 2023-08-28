def nome_composto():
    nome = input("Insira seu 1º nome: ")
    sobrenome = input("Insira seu 2º nome: ")
    return nome.upper(), sobrenome.lower()

print(nome_composto())