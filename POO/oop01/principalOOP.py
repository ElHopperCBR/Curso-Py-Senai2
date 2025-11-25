import trianguloOOP as tl
#Instanciar a classe
trianguloX = tl.triangulo()
trianguloY  = tl.triangulo()
#Entrada de dados
print("Digite as medidas do triangulo X:")
trianguloX.a = int(input("Digite a medida a: "))
trianguloX.b = int(input("Digite a medida b: "))
trianguloX.c = int(input("Digite a medida c: "))
print("Digite as medidas do triangulo Y:")
trianguloY.a = int(input("Digite a medida a: "))
trianguloY.b = int(input("Digite a medida b: "))
trianguloY.c = int(input("Digite a medida c: "))
#Processamento de dados
areax = trianguloX.area()
areay = trianguloY.area()
#Condicional para verificar qual triangulo eh maior
if areax > areay :
    saida = "A area do triangulo X eh maior que a area do triangulo Y"
elif areay > areax :
    saida = "A area do triangulo Y eh maior que a area do triangulo X"
else:
    saida = "As areas dos triangulos X e Y sao iguais"
#Saida de dados
print(f"A area do triangulo X = {areax:.1f}")
print(f"A area do triangulo Y = {areay:.1f}")
print(saida)