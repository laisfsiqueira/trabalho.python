#FUAQ que leia uma temperatura em graus Celsius e mostrea convertida 
# em graus Fahrenheit. A fórmula de conversão é: 
# F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

celsius = int(input("Digite os graus em celsius: "))
fahrenheit = ((celsius + 160) / 5)

print(f"{celsius}C é equivalente a {fahrenheit}F")