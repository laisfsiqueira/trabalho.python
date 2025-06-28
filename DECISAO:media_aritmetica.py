# Leia 3 notas de um aluno e em seguida calcule a média aritmética
# e mostre, além do valor da média

nota1 = float(input("Informe primeira nota: "))
nota2 = float(input("Informe segunda nota: "))
nota3 = float(input("Informe terceira nota: "))

media = (nota1 + nota2 + nota3)/3
print(media)

if media >= 7.0 :
    print("Aprovado!")
elif media <= 7.0 and media >= 3.0:
    print("recuperação")
elif media < 3.0:
    print("reprovado")
else:
    print("resultado: ")