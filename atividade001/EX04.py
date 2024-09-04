def verificar_numero(num):

    unidades = {
        1: "um",
        2: "dois",
        3: "tres",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
    }

    diferentes = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
    }

    dezenas = {
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "sessenta",
        80: "oitenta",
        90: "noventa",
    }


    if num in unidades:
        return unidades[num]
    elif num in diferentes:
        return diferentes[num]
    else:
        dezena = (int(num) // 10) * 10
        unidade = int(num) % 10
        if unidade == 0:
            return dezenas[dezena]
        else:
            return f'{dezenas[dezena]} e {unidades[unidade]}'


def main():
    num = int(input("Informe um número para ser escrito por extenso: "))
    print(verificar_numero(num))



main()

