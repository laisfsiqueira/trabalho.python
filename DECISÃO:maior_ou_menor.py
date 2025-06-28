# Leia dois valores inteiros e diferentes em seguida
# apresenta o MAIOR e o MENOR número

valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))

if valor1 > valor2:
  print("maior:", valor1)
  print("menor:", valor2)
else:
  print("maior:", valor2)
  print("menor:", valor1)