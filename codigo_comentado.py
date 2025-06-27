# Importa o módulo 'os' para executar comandos do sistema operacional
import os
# Importa o módulo 'signal' para trabalhar com sinais do sistema (como timeouts)
import signal

# Define uma função que será chamada quando o timeout (alarme) for acionado
def timeout(signum, frame):
    # Lança uma exceção genérica com a mensagem 'ERRO' quando o tempo limite é atingido
    raise Exception('ERRO')

# Configura o sistema para chamar a função 'timeout' quando receber o sinal SIGALRM
signal.signal(signal.SIGALRM, timeout)
# Define um alarme de 15 segundos - após esse tempo, a função timeout será executada
signal.alarm(15)

# Inicia um loop infinito - o programa roda continuamente até ser interrompido
while True:
    # Limpa a tela do terminal (comando 'clear' do Linux/Mac)
    os.system('clear')
    # Imprime o título do sistema
    print("Sistema de vendas.")
    # Imprime instruções de como iniciar uma venda
    print("Para iniciar uma venda começe pelo comando inicio.")
    # Imprime instruções de como adicionar um item (formato: venda;produto;valor)
    print("Para adicionar um item digite venda;produto;valor.")
    # Imprime instruções de como cancelar um produto (formato: cancela;produto)
    print("Para cancelar um produto digite cancela;produto")
    # Imprime instruções de como finalizar a venda
    print("Para finalizar a venda digite fim.")

    # Inicia um bloco try-except para capturar exceções (principalmente timeout)
    try:
        # Reinicia o alarme de 15 segundos antes de aguardar input do usuário
        signal.alarm(15)
        # Aguarda input do usuário e armazena na variável 'i'
        i = input()
        # Converte o input para maiúsculas (padronização)
        i = i.upper()
        # Cancela o alarme pois o usuário digitou algo dentro do tempo limite
        signal.alarm(0)
    # Captura qualquer exceção (principalmente a do timeout)
    except Exception:
        # Imprime mensagem de erro
        print("ERRO")
        # Encerra o programa
        exit()

    # Verifica se o usuário digitou "INICIO" para começar uma venda
    if i == "INICIO":
        # Cria uma lista vazia para armazenar os nomes dos produtos
        prod = []
        # Cria uma lista vazia para armazenar os valores dos produtos
        valor = []
        
        # Inicia outro loop infinito para processar comandos da venda
        while True:
            # Inicia bloco try-except para capturar timeout durante a venda
            try:
                # Reinicia o alarme de 15 segundos
                signal.alarm(15)
                # Aguarda input do usuário para comandos da venda
                comando = input()
                # Converte para maiúsculas
                comando = comando.upper()
                # Divide o comando pelos pontos e vírgulas (formato: AÇÃO;PRODUTO;VALOR)
                comando = comando.split(';')
                # Cancela o alarme
                signal.alarm(0)
            # Captura exceção de timeout
            except Exception:
                # Imprime erro e encerra o programa
                print("ERRO")
                exit()
            
            # Verifica se o primeiro elemento do comando é "VENDA"
            if comando[0] == "VENDA":
                # Inicia bloco try-except para validar o nome do produto
                try:
                    # Verifica se o produto já existe na lista de produtos
                    if comando[1] in prod:
                        # Se já existe, imprime erro e encerra programa
                        print("ERRO")
                        exit()
                    else:
                        # Se não existe, adiciona o produto à lista
                        prod.append(comando[1])
                # Captura erro se não foi fornecido nome do produto (índice 1 não existe)
                except IndexError:
                    print("ERRO!")
                    print("Nome do produto não inserido.")
                    exit()
                
                # Inicia bloco try-except para validar o valor do produto
                try:
                    # Tenta converter o terceiro elemento (valor) para float
                    comando[2] = float(comando[2])
                    # Verifica se o valor é maior que 0
                    if comando[2] > 0:
                        # Se válido, adiciona à lista de valores
                        valor.append(comando[2])
                    else:
                        # Se valor é 0 ou negativo, imprime erro e encerra
                        print("ERRO!")
                        print("Valor do produto não pode ser 0 ou negativo.")
                        exit()
                # Captura erro se o valor não for numérico
                except ValueError:
                    print("ERRO!")
                    print("Valor do produto deve ser numerico. Ex: 4.90")
                    exit()
                # Captura erro se não foi fornecido valor (índice 2 não existe)
                except IndexError:
                    print("ERRO!")
                    print("Valor do produto não inserido.")
                    exit()
            
            # Verifica se o comando é para cancelar um produto
            elif comando[0] == "CANCELA":
                # Inicia bloco try-except genérico para cancelamento
                try:
                    # Encontra o índice do produto na lista
                    indice = prod.index(comando[1])
                    # Remove o produto da lista de produtos
                    prod.remove(comando[1])
                    # Remove o valor correspondente da lista de valores usando o índice
                    valor.pop(indice)
                # Captura qualquer erro (produto não encontrado, índice inválido, etc.)
                except:
                    print("ERRO!")
                    print("Produto não cadastrado!")
                    exit()
            
            # Verifica se o comando é para finalizar a venda
            elif comando[0] == "FIM":
                # Verifica se o total da venda é 0 (sem produtos)
                if sum(valor) == 0:
                    print("ERRO")
                    exit()
                # Calcula o total da venda
                total = sum(valor)
                # Imprime o total arredondado para 2 casas decimais
                print(round(total,2))
                # Encerra o programa
                exit()
    
    # Se o usuário não digitou "INICIO"
    else:
        # Imprime mensagem de erro
        print("ERRO!")
        # Instrui o usuário e aguarda uma tecla
        print("Para iniciar digite inicio. Pressione qualquer tecla para continuar.")
        input()  # Aguarda o usuário pressionar qualquer tecla
        # Limpa a tela
        os.system('clear')
        # Encerra o programa
        exit()