#Problema triangulo sem oop
#Entrada de dados
#TRIANGULO X
print("Inserir as medidas do triangulo X")
ax = int(input("Digite a medida a:"))
bx = int(input("Digite a medida b:"))
cx = int(input("Digite a medida c:"))
#TRIANGULO Y
print("Inserir as medidas do triangulo Y")
ay = int(input("Digite a medida a: "))
by = int(input("Digite a medida b: "))
cy = int(input("Digite a medida c: "))
#Processamento de dados
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5
p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5
#Condicional para verificar qual triangulo eh maior
if areax > areay :
    saida = "A area do triangulo X eh maior que a area do triangulo Y"
elif areay > areax:
    saida = "A area do triangulo Y eh maior que a area do triangulo X"
else:
    saida = "As areas dos triangulos sao iguais"
#Saida de dados
print(f"A area do triangulo X = {areax:.1f}")
print(f"A area do triangulo Y = {areay:.1f}")
print(saida)