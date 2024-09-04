def resposta():

    resposta = input("Informe a palavra ou frase para saber se ela é palíndroma ou não:").strip().upper()
    resposta2 = resposta.replace(' ', '')
    inverter_frase(resposta2)


def inverter_frase(resposta2):
    invertida = resposta2[::-1]
    checagem(resposta2, invertida)


def checagem(resposta2, invertida):
    if invertida == resposta2:
        print("A palavra/frase é palindroma")
    else:
        print("A palavra/frase não é palindroma")


def main():
    resposta()


main()















