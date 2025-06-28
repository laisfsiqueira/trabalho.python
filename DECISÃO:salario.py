'''
Leia o salário e o cargo de um funcionário e calcule o novo salário.

Código 	    Cargo	      Percentual 
  101   	 Gerente	       10%
  102	    Engenheiro	     20%
  103	     Técnico	       30%

'''

# digitar o salario e o cargo

salario = float(input("digite o salario do funcionario: "))
cargo = int(input("digite o código do cargo do funcionario: "))

if cargo == 101:
    porcentagem = salario * 0.1
elif cargo == 102:
    porcentagem = salario * 0.2
elif cargo == 103:
    porcentagem = salario * 0.3
else:
    porcentagem = salario * 0.4

# Mostre o salário antigo, o novo salário e a diferença

salario_antigo = salario
salario_novo = (salario * porcentagem) + salario
diferenca_salario = salario_novo - salario_antigo

print(f"o salario era: {salario_antigo}")
print(f"o salario novo é: {salario_novo}")
print(f"a difença de aumento no salario é: {diferenca_salario}")