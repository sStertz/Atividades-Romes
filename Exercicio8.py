def opções():
    option_1 = "1. Conte o número de palavras digitadas."
    option_2 = "2. Conte o número de vogais digitadas."
    option_3 = "3. Substitua a palavra Python por Java."
    option_4 = "4. Converta todas as letras em minúsculas."
    option_5 = "5. Crie uma lista com todas as palavras únicas encontradas."
    option_6 = "6. Imprima em ordem alfabética."
    print("OPÇÕES DO MENU: ")
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    print(option_6)
    option_selector = input("Qual opção deseja: ")
    menu_selector(int(option_selector))

def menu_selector(option_selector):
    if option_selector >= 1 or option_selector <= 6:
        texto = input("digite uma palavra ou frase: ")

        if option_selector == 1:
            print("Função: 1")
            print(len(texto))

        elif option_selector == 2:
            print("Função: 2")
            print(texto.count('a')+texto.count('e')+texto.count('i')+texto.count('o')+texto.count('u'))

        elif option_selector == 3:
            print("Função: 3")
            print(texto.lower().replace('python', 'java'))

        elif option_selector == 4:
            print("Função: 4")
            print(texto.lower())

        elif option_selector == 5:
            print("Função: 5")
            print(list(set(texto.lower().split())))

        elif option_selector == 6:
            print("Função: 6")
            print(sorted(texto.split()))
    

opções()
