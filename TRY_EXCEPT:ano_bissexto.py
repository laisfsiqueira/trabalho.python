# Solicita a data ao usuário
try:
    day = int(input("Digite o dia: "))
    month = int(input("Digite o mês: "))
    year = int(input("Digite o ano: "))

    # Verifica se o ano está entre 0 e 3000
    if 0 <= year <= 3000:
        # Verifica se o mês está entre 1 e 12
        if 1 <= month <= 12:
            # Verifica o número de dias com base no mês
            if month == 2:
                # Verifica se é bissexto
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if 1 <= day <= 29:
                        print("A data é válida.")
                    else:
                        print("A data é inválida.")
                else:
                    if 1 <= day <= 28:
                        print("A data é válida.")
                    else:
                        print("A data é inválida.")
            elif month in [4, 6, 9, 11]:
                if 1 <= day <= 30:
                    print("A data é válida.")
                else:
                    print("A data é inválida.")
            else:
                if 1 <= day <= 31:
                    print("A data é válida.")
                else:
                    print("A data é inválida.")
        else:
            print("A data é inválida.")
    else:
        print("A data é inválida.")
except ValueError:
    print("Por favor, insira valores numéricos para dia, mês e ano.")