ano_max = int(input("Digite o ano máximo (até 4000): "))

def anosV():
    return ano_max < 2000 or ano_max > 4000

if anosV():
    print('Digite um ano válido!')
else:
    contador = 0
    for ano in range(2000, ano_max + 1):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            contador += 1
    print("Quantidade de anos bissextos:", contador)