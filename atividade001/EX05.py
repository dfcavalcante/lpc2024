import random


with open("forca.txt", "r") as arquivo:
    palavras = arquivo.readlines()
    num_aleatorio = random.randint(0, len(palavras) - 1)
    palavra_forca = palavras[num_aleatorio].strip().upper()
    palavra_secreta = "_" * len(palavra_forca)
    print(palavra_forca)

def preencher_palavra(acertos):
    global palavra_secreta, palavra_forca
    palavra_secreta = palavra_forca
    for letra in palavra_secreta:
        if letra not in acertos:
            palavra_secreta = palavra_secreta.replace(letra, "_")


def descobrir_palavra():
    erros = 0
    acertos = []
    print("Forca com o Tema: Cores")
    global palavra_secreta, num_aleatorio, palavra_forca
    while erros <= 6:
        chute = input("Digite uma letra: ")
        chute = chute.upper()
        if erros == 6:
            print("Você perdeu.")
            break
        if chute in palavra_forca:
            acertos.append(chute)
            preencher_palavra(acertos)
            if palavra_secreta == palavra_forca:
                print("Você ganhou!")
                print(f"Palavra secreta: {palavra_forca}")
                break
        else:
            if erros == 6:
                print("Você perdeu.")
                break
            else:
                erros +=1
        print(palavra_secreta)
        print(f"Erros: {erros}. Limite de erros: 6")





descobrir_palavra()

