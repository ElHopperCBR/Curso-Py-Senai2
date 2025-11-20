from typing import final

@final
class Forma(object): # Classe selada (não pode ser herdada)
    cor: str
    def __init__(self, cor):
        self.cor = cor

@final
def calcular_area(self): # Método selado (não pode ser sobrescrito)
    return "Área não especificada"
class Circulo(Forma):
    raio: float
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self): # Erro de tempo de compilação ou runtime, dependendo do contexto
        return f"Área do círculo: {3.14 * self.raio ** 2}"
# Tentativas de herança e sobrescrita (que falhariam ou dariam erro)
# c = Circulo("vermelho", 5) # A definição de Circulo falharia por ser @final
# c.calcular_area() # A chamada também falharia por ser um método @final

forma = Forma("azul")
print(f"Cor da forma: {forma.cor}")

circulo = Circulo("vermelho", 5)
print(circulo.calcular_area())