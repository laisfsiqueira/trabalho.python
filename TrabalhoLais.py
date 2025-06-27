import os
import signal

def timeout(signum, frame):
    raise Exception('ERRO')

signal.signal(signal.SIGALRM, timeout)
signal.alarm(15)

while True:
  os.system('clear')
  print("Sistema de vendas.")
  print("Para iniciar uma venda começe pelo comando inicio.")
  print("Para adicionar um item digite venda;produto;valor.")
  print("Para cancelar um produto digite cancela;produto")
  print("Para finalizar a venda digite fim.")


  try:
      signal.alarm(15)
      i = input()
      i = i.upper()
      signal.alarm(0)
  except Exception:
      print("ERRO")
      exit()

  if i == "INICIO":
      prod = []
      valor = []
      while True:
          try:
              signal.alarm(15)
              comando = input()
              comando = comando.upper()
              comando = comando.split(';')
              signal.alarm(0)
          except Exception:
              print("ERRO")
              exit()
          if comando[0] == "VENDA":
              try:
                  if comando[1] in prod:
                      print("ERRO")
                      exit()
                  else:
                      prod.append(comando[1])
              except IndexError:
                  print("ERRO!")
                  print("Nome do produto não inserido.")
                  exit()
              try:
                  comando[2] = float(comando[2])
                  if comando[2] > 0:
                      valor.append(comando[2])
                  else:
                      print("ERRO!")
                      print("Valor do produto não pode ser 0 ou negativo.")
                      exit()
              except ValueError:
                  print("ERRO!")
                  print("Valor do produto deve ser numerico. Ex: 4.90")
                  exit()
              except IndexError:
                  print("ERRO!")
                  print("Valor do produto não inserido.")
                  exit()
          elif comando[0] == "CANCELA":
              try:
                  indice = prod.index(comando[1])
                  prod.remove(comando[1])
                  valor.pop(indice)
              except:
                  print("ERRO!")
                  print("Produto não cadastrado!")
                  exit()
          elif comando[0] == "FIM":
              if sum(valor) == 0:
                  print("ERRO")
                  exit()
              total = sum(valor)
              print(round(total,2))
              exit()
  else:
      print("ERRO!")
      print("Para iniciar digite inicio. Pressione qualquer tecla para continuar."); input()
      os.system('clear')
      exit()