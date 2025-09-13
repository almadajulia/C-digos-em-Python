dia = int(input('Dia do nascimento: '))
mes = int(input('Mês do nascimento: '))
ano = int(input('Ano do nascimento: '))
idade = 2025 - ano
if mes > 8:
    idade -= 1
elif mes == 8 and dia > 8:
    idade -= 1
print(f"A sua idade é: {idade} anos.")