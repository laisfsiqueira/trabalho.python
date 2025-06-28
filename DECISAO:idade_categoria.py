# Leia a idade de um nadador e a seguir classifique-o 
# em uma das seguintes categorias

# infantil A	 5 - 7 anos 
# infantil B 	 8-10 anos
# juvenil A 	 11-13 anos 
# juvenil B 	 14-17 anos 
# adulto	 maiores de 18 anos 

# Leia a idade do nadador
idade = int(input("digite a idade do nadador: "))

# Classifique o nadador
if idade >= 5 and idade <= 7:
  print("categoria: infantil A")
elif idade >= 8 and idade <= 10:
  print("categoria: infantil B")
elif idade >= 11 and idade <= 13:
  print("categoria: juvenil A")
elif idade >= 14 and idade <= 17:
  print("categoria: juvenil B")
elif idade < 5:
  print("idade inadequada!")
elif idade >= 18:
  print("categoria: adulto")
else:
  print(f"A categoria do nadador é: {idade}")

