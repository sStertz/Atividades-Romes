def juntar_nome():
    nome = input("Insira seu nome completo: ")
    frag_nome = nome.split()
    nome_parte = frag_nome[0]
    sobrenome = " ".join(nome_parte[1:])
    nome_completo = nome.upper()
    tamanho_nome = len(nome)
    print(nome.lower())
    print("Seu nome tem: "+ str(tamanho_nome) + " caractéres.")

print(juntar_nome())