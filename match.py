dia = int(input("Digite o dia da semana de 1 a 7: "))

match dia:
    case 1:
      print("doming")
    case 2:
      print("segunda")
    case 3:
      print("terça")
    case 4:
      print("quarta")
    case 5:
      print("quinta")
    case 6:
      print("sexta")
    case 7:
      print("sabado")
    case other:
      print("dia invalido")