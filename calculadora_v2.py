# Calculadora em Python

print("\n")
pc = ' Python Calculator '
print(pc.center(120, "*"))

print("\nSelecione o Número da Operação Desejada:")

print("\n1 - Soma")

print("2 - Subtração")

print("3 - Multiplicação")

print("4 - Divisão")

print("5 - Exponencial")

operacao = int(input("\nDigite a sua opção (digite 1/2/3/4/5): "))
primeirovalor = float(input("\nDigite o primeiro valor: "))
segundovalor = float(input("\nDigite o segundo valor: "))

def calculadora(primeirovalor, segundovalor):
    if operacao == 1:
        soma = primeirovalor + segundovalor
        print("\n\nResultado: ", str(primeirovalor), " + ", str(segundovalor), " = ", str(round(soma,3)))
    
    elif operacao == 2:
        subtracao = primeirovalor - segundovalor
        print("\n\nResultado: ", str(primeirovalor), " - ", str(segundovalor), " = ", str(round(subtracao,3)))
        
    elif operacao == 3:
        multiplicacao = primeirovalor * segundovalor
        print("\n\nResultado: ", str(primeirovalor), " * ", str(segundovalor), " = ", str(round(multiplicacao,3)))
    
    elif operacao == 4:
        divisao = primeirovalor / segundovalor
        print("\n\nResultado: ", str(primeirovalor), " / ", str(segundovalor), " = ", str(round(divisao,3)))
        
    elif operacao == 5:
        exponencial = primeirovalor ** segundovalor
        print("\n\nResultado: ", str(primeirovalor), " ^ ", str(segundovalor), " = ", str(round(exponencial,3)))

    else:
        print("\n\nNão há esta opção!")
        
calculadora(primeirovalor, segundovalor)
        
print("\n")
ed = ' End '
print(ed.center(120, "*"))
