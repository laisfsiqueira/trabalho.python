# Leia um número correspondendo a uma quantidade de dias e após,
# calcule e mostre a quantidade de anos, meses e dias correspondentes.
# Para facilitar o cálculo, considere ano com 365 dias e mês com 30 dias

dias = int(input("Digite a quantidade de dias: "))

# um ano tem 365 dias
anos = dias // 365
resto = dias - (365 * anos)

# um mes tem 30 dias
meses =  dias // 30
resto = dias - (30 * meses)

print("Anos", anos)
print("Meses", meses)
print("Dias", dias)