# Calcule a quantidade de cerveja, em litros, consumida por um bloco de carnaval. 
# Para isso considere que uma garrafa de cerveja possui 600ml e
# uma caixa possui 24 garrafas.
# O algortimo deverá ler a quantidade de caixas consumidas
# e retornar a quantidade equivalente em litros.

# uma caixa tem 24 garrafas e 600ml equivale a 0.6L
total_caixas = int(input("Digite a quantidade de caixas: "))
input = total_caixas * 24 * 0.6

print(f"A quantidade de cerveja consumida é de {input} litros")