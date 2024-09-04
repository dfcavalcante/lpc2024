def verificacao_formato(cpf):
    if len(cpf) != 14:
        return False

    if cpf[3] and cpf[7] != ".":
        return False

    if  cpf[11] != "-":
        return False

    return True


def calculo(cpf):

    #Primeiro digito
    soma1 = 0
    cpf = cpf.replace("-", "").replace(".", "")
    for i in range(len(cpf) - 2):
        soma1 += int(cpf[i]) * (10 - i)
    resto1 = soma1 % 11
    primeiro_digito = 11 - resto1
    if primeiro_digito >= 10:
        primeiro_digito = 0

    #Segundo digito
    soma2 = 0
    for i in range(len(cpf) - 1):
        soma2 += int(cpf[i]) * (11 - i)
    resto2 = soma2 % 11
    segundo_digito = 11 - resto2
    if segundo_digito >= 10:
        segundo_digito = 0

    validacao(primeiro_digito, segundo_digito, cpf)


def validacao(primeiro_digito, segundo_digito, cpf):
    if primeiro_digito != int(cpf[9]):
        print("CPF inválido.")
    elif segundo_digito != int(cpf[10]):
        print("CPF inválido.")
    else:
        print(f"O CPF {cpf} é valido.")


def main():
    cpf = input('Digite o CPF no formato xxx.xxx.xxx-xx: ')
    verificacao_formato(cpf)
    calculo(cpf)




main()









