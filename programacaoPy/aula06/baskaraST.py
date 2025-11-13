from streamlit import header,write,text_input,button,warning,success,error
from math import sqrt,pow
#Função python
def calculo(deltaClodoaldo):
    valor = (sqrt(deltaClodoaldo)) / (2*a)
    return valor

#Função python
header('Calculadora de Bhaskara')
write("Calculadora de raízes \n\n de uma equação de segundo grau")
write("ax² + bx + c = 0")
#Entrada de dados
a = text_input('Digite o valor de a:', icon='🅰️')
b = text_input('Digite o valor de b:', icon='➖')
c = text_input('Digite o valor de c:',icon='➕')
#Processamento de dados
if button('Calcular raízes'):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta = pow(b,2) - 4*a*c
        if delta < 0:
            warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz = (-b + calculo(delta))
            success(f"A equação possui uma raiz real: {raiz}")
        else:
            raiz1 = (-b + calculo(delta))
            raiz2 = (-b - calculo(delta))
            success(f"As raízes da equação são: \n\n Raiz 1: {raiz1} \n\n Raiz 2: {raiz2}")
    except ValueError:
        error("Por favor, insira valores válidos para a, b e c.")
    except ZeroDivisionError:
        error("O valor de 'a' não pode ser zero em uma equação de segundo grau.")
