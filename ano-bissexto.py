def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

input_year = int(input("Digite um ano final (maior ou igual a 2000): "))

def validate_year():
    return input_year <= 4000 and input_year > 2000  

if not validate_year():
    print("O ano deve ser 2000 ou maior.")
else:
    leap_years = 0
    for year in range(2000, input_year + 1):
        if is_leap_year(year):
            leap_years += 1

    print(f"De 2000 até {input_year}, existem {leap_years} anos bissextos.")
