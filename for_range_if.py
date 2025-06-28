# FUAQ que receba dois valores, faça e mostre a soma deles 10 vezes

valor_1 = 0
valor_2 = 0
intervalo = 0
soma = 0

for intervalo in range(1,11,1):
  print(f"Execução de numero {intervalo}")
  if intervalo == 1:
    valor_1 = int(input("Digite o primeiro valor "))
    valor_2 = int(input("Digite o segundoo valor "))
  elif intervalo >= 1 and intervalo < 2:
    soma = int(valor_1) + int(valor_2)
  elif intervalo >= 2 and intervalo <= 10:
    t = soma
    soma = sum(t,soma)
  print(f"A soma dos valores é igual: {soma}")