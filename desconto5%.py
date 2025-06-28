# FUAQ receba um valor de um produto e que escreva o novo valor 
# tendo em vista que o desconto foi de 5%.

valor = float(input("Digite o valor: "))
valor_desconto = valor - (valor * 0.70)

print(f"novo valor: R$ {valor_desconto}")
