'''
 Ler um valor em reais e mostrar qual o número de notas de 100, 50, 20, 10, 5 e 2
 em que o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas
 necessárias.
'''

valor = int(input("Informe valor: "))

notas100 = int(valor / 100)
resto = valor - (notas100 * 100)

notas50 = int(resto / 50)
resto = resto - (notas50 * 50)

notas20 = int(resto / 20)
resto = resto - (notas20 * 20)

notas10 = int(resto / 10)
resto = resto - (notas10 * 10)

# verifica se distribui cedulas de R$5
notas5 = 0
if (resto % 2 != 0):
    notas5 = int(resto / 5)
    resto = resto - (notas5 * 5)

notas2 = int(resto / 2)
resto = resto - (notas2 * 2)

txt = "Notas R$100={}, notas R$50={}, notasR$20={}, notas R$10={}, notas R$5={}, notas R$2={}"
print(txt.format(notas100, notas50, notas20, notas10, notas5, notas2))        