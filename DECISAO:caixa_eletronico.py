'''
 Ler um valor em reais e mostrar qual o número de notas de 100, 50, 20, 10, 5 e 2
 em que o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas
 necessárias.
'''
valor = int(input("digite um valor: "))

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0

if valor == 3:
    print("ERROR")
    exit()
if valor >= 100:
    nota_100 = (valor // 100)
    valor = valor % 100
if valor == 73:
    nota_2 = 4 
    valor = 65 
if valor == 53:
    nota_2 = 4 
    valor = 45 
if valor >= 50:
    nota_50 = (valor // 50)
    valor = valor % 50
if valor == 43:
    nota_2 = 4 
    valor = 35 
if valor == 33:
    nota_2 = 4 
    valor = 25 
if valor == 23:
    nota_2 = 4
    valor = 15
if valor >= 20:
    nota_20 = (valor // 20)
    valor = valor % 20
if valor == 13:
    nota_5 = 1
    valor = 8
if valor == 11:
    nota_5 = 1
    valor = 6
if valor >= 10:
    nota_10 = (valor // 10)
    valor = valor % 10
if valor == 8:
    nota_2 = valor // 2
    valor = valor %2
if valor == 6:
    nota_2 = valor // 2
    valor = valor %2
if valor >= 5:
    nota_5 = (valor // 5)
    valor = valor % 5
if valor >= 2:
    nota_2 = (valor // 2)
    valor = valor % 2
 
print(f"são necessarias {nota_100} notas de R$ 100")
print(f"são necessarias {nota_50} notas de R$ 50")
print(f"são necessarias {nota_20} notas de R$ 20")
print(f"são necessarias {nota_10} notas de R$ 10")
print(f"são necessarias {nota_5} notas de R$ 5")
print(f"são necessarias {nota_2} notas de R$ 2")