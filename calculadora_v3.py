# Calculadora em Python 

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n")
pc = ' Python Calculator '
print(pc.center(120, "*"))

print("\nSelecione o Número da Operação Desejada:")

print("\n1 - Soma")

print("2 - Subtração")

print("3 - Multiplicação")

print("4 - Divisão")

print("5 - Exponencial")

op = int(input("\nDigite a sua opção (digite 1/2/3/4/5): "))
num = input("\nDigite os números com espaços entre eles: ")
val = list(map(float, num.split()))

print("\nValores da operação: ", val)

def calculadora(val):
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
        for i in val[1:]:
            val[0] /= i
        print("\n\nResultado Divisão = ", str(round(val[0],3)))
    elif op == 5:
        for i in val[1:]:
            val[0] **= i
        print("\n\nResultado Exponencial = ", str(round(val[0],3)))
    else:
        print("\n\nNão há esta opção!")
calculadora(val)  

print("\n")
ed = ' End '
print(ed.center(120, "*"))
