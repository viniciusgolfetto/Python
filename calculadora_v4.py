# CALCULADORA em PYTHON

# Início com um espaçamento para o cabeçalho, determinando uma variável 'pc' como título e a centralizo complementando com '*' a linha toda.
print("\n")
pc = ' Python Calculator '
print(pc.center(120, "*"))

# Mostrando as operações que podem ser feitas.
print("\nSelecione o Número da Operação Desejada:")

print("\n1 - Soma")

print("2 - Subtração")

print("3 - Multiplicação")

print("4 - Divisão")

print("5 - Exponencial")

print("6 - Raíz Quadrada")

# Tratamento de erros. O código garante que para a variável 'op' será digitado somento os valores inteiros entre 1 a 5 e garante que somente
# na variável 'num' seja inserido números.
while True:
    try:
        op = int(input("\nDigite a sua opção (digite 1/2/3/4/5/6): "))
        if  (op < 1) or (op > 6):
            print("\nNúmero Invalido! Tente novamente!")
            continue
    except:
        print("\nVocê não digitou um número! Tente novamente!")
        continue
    else:
        print("\nOperação válida!")
        break
        
while True:
    try:
        num = input("\nDigite os números para realizar a operação com espaçamento entre eles: ")
    except:
        print("\nHá caracter(es) além de números!")
        continue
    else:
        print("\nNúmeros válidos!") 
        val = list(map(float, num.split()))         # A variável 'val' me retorna uma lista de números através da variável 'num'.
        print("\nValores da operação: ", val)       # Mostro os valores digitados.
        break

# Defino a função 'def operacao(val):' com duas variáveis locais ('vals' e 'valus') para fazer as operações solicitadas.
# Importando do pacote 'math' o módulo 'sqrt'
from math import sqrt

def operacao(val):
    vals = 0; valus = 1
    if op == 1:
        for i in val:
            vals += i
        print("\n\nResultado Soma = ", str(round(vals,3)))
    elif op == 2:
        for i in val[1:]:
            val[0] -= i
        print("\n\nResultado Subtração = ", str(round(val[0],3)))
    elif op == 3:
        for i in val:
            valus *= i
        print("\n\nResultado Multiplicação = ", str(round(valus,3)))
    elif op == 4:
        try:
            for i in val[1:]:
                val[0] /= i
            print("\n\nResultado Divisão = ", str(round(val[0],3)))
        except ZeroDivisionError:
            print("\n\nERRO: Não é possível dividir qualquer número por 0!")
    elif op == 5:
        for i in val[1:]:
            val[0] **= i
        print("\n\nResultado Exponencial = ", str(round(val[0],3)))
    elif op == 6:
        try:
            print("\n\nResultado Raíz Quadrada = ", str(round(sqrt(val[0]),3)))
        except ValueError:
            print("\n\nERRO: Não é possível obter a raíz quadrada de um número negativo!")
    else:
        print("\n\nNão há esta opção!")
operacao(val)  

# Concluo determinando uma variável 'ed' como título final da operação e o centralizo complementando com '*' a linha toda.
print("\n")
ed = ' End '
print(ed.center(120, "*"))