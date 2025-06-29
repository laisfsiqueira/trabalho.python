'''
Leia 3 valores inteiros e diferentes e a seguir, encontre
e exiba o maior, o menor e o intermediário.
'''

valor_1 = int(input("digite o primeiro valor: "))
valor_2 = int(input("digite o segundo valor: "))
valor_3 = int(input("digite o terceiro valor: "))

if valor_1 > valor_2 and valor_1 > valor_3:
    maior = valor_1
elif valor_2 > valor_1 and valor_2 > valor_3:
    maior = valor_2
elif valor_3 > valor_1 and valor_3 > valor_2:
    maior = valor_3
    
if valor_1 < valor_2 and valor_1 < valor_3:
    menor = valor_1
elif valor_2 < valor_1 and valor_2 < valor_3:
    menor = valor_2
elif valor_3 < valor_1 and valor_3 < valor_2:
    menor = valor_3

meio = (valor_1 + valor_2 + valor_3 ) - (maior + menor)

print("valor maior", maior)
print("valor menor", menor)
print("valor intermediario", meio)