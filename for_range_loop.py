# FUAQ que receba dois valores, faça e mostre a soma deles 10 vezes

for intervalo in range(1,11,1):
    print(f"Execução de numero {intervalo}")
    valor_1 = int(input("Digite o primeiro valor: "))
    valor_2 = int(input("Digite o segundoo valor: "))
    soma = valor_1 + valor_2
    print(f"A soma dos valores é igual: {soma}")
