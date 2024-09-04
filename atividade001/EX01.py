import random


def lancar_dado(registrador):
    for i in range(100):
        resultado = random.randint(1,6)
        registrador.append(resultado)



def contador(registrador):
    qntd1 = 0
    qntd2 = 0
    qntd3 = 0
    qntd4 = 0
    qntd5 = 0
    qntd6 = 0
    for i in range(len(registrador)):
        resultado = registrador[i]
        if resultado == 1:
            qntd1 += 1
        elif resultado == 2:
            qntd2 += 1
        elif resultado == 3:
            qntd3 += 1
        elif resultado == 4:
            qntd4 += 1
        elif resultado == 5:
            qntd5 += 1
        elif resultado == 6:
            qntd6 += 1
    print(f"""
    O lançamento do dado foi 1: {qntd1} vezes
    O lançamento do dado foi 2: {qntd2} vezes
    O lançamento do dado foi 3: {qntd3} vezes
    O lançamento do dado foi 4: {qntd4} vezes
    O lançamento do dado foi 5: {qntd5} vezes
    O lançamento do dado foi 6: {qntd6} vezes
""")


def main():
    registrador = []
    lancar_dado(registrador)
    contador(registrador)


main()







