class Cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

Numlado = Cuadrado(50)
print("El area del cuadrado es:", Numlado.area())
