'''
Calcule o imposto de renda de um contribuinte, onde o usuário informe o valor anual recebido e o
sistema mostra o cálculo do imposto de renda de acordo com a tabela progressiva abaixo.

Até 17.989,80	–                 %
De 17.989,81 até 26.961,00	   7,5
De 26.961,01 até 35.948,40	  15,0
De 35.948,41 até 44.918,28	  22,5
Acima de 44.918,28	          27,5

'''

valor_anual = float(input("Digite o valor anual: "))

if valor_anual <= 17.989:
    print("isento")
    ir = 0
elif valor_anual >= 17.989 and valor_anual <= 26.961:
    categoria = "7.5%"
    ir = 0.075 * valor_anual
elif valor_anual >= 26.961 and valor_anual <= 35.948:
    categoria = "15%"
    ir = 0.15 * valor_anual
elif valor_anual >= 35.948 and valor_anual <= 44.918:
    categoria = "22.5%"
    ir = 0.225 * valor_anual
elif valor_anual >= 44.918:
    categoria = "27.5%"
    ir = 0.275 * valor_anual

print(f"O total a pagar do IR {ir}")