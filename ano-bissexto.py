def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano_final = int(input("Digite um ano final (maior ou igual a 2000): "))

def valida_ano():
  return ano_final < 2000

if valida_ano():
    print("O ano deve ser 2000 ou maior.")
else:
    bissextos = 0
    for ano in range(2000, ano_final + 1):
        if eh_bissexto(ano):
            bissextos += 1

    print(f"De 2000 até {ano_final}, existem {bissextos} anos bissextos.")
