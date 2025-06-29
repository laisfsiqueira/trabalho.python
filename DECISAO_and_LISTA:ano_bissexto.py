'''
Leia uma data informada pelo usuário (dia, mês e ano)

• O valor de ano está entre 0 e 3000.
• O valor de mês está entre 1 e 12
• O valor de dia:
– está entre 1 e 28 no mês de fevereiro em anos não bissextos.
– Está entre 1 e 29 no mês de fevereiro em anos bissextos.
– Está entre 1 e 30 nos meses de abril, junho, setembro e novembro.
– Está entre 1 e 31 nos demais casos, janeiro, março, maio, julho, agosto, 
outubro, dezembro


'''
          
# Verifica se o ano está entre 0 e 3000
ano = int(input("digite o ano: "))

if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
  anob = True
else:
  anob = False

if ano >= 0 and ano <= 3000:
# Verifica se o mês está entre 1 e 12
  mes = int(input("digite o mes: "))
  
  meses31dias = [1,3,5,7,8,10,12]
  meses30dias = [4,6,9,11]
  
  if mes in meses31dias:
    dia = int(input("digite o dia de 1 a 31: "))
    if mes <1 or mes > 31:
      exit()
    if anob == True:
      print("Ano é bissexto.")
    else:
      print("Ano não é bissexto.")
  elif mes in meses30dias:
    dia = int(input("digite o dia de 1 a 30: "))
    if mes <1 or mes > 30:
      exit()
    if anob == True:
      print("Ano é bissexto.")
    else:
      print("Ano não é bissexto.")
  elif mes == 2:
    if anob == True:
      dia = int(input("digite o dia de 1 a 29: "))
      print("Ano Bissexto.")
    else:
      dia = int(input("digite o dia de 1 a 28: "))
      print("Ano não é bissexto.")
