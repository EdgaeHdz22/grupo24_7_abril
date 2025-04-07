class Cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

Numlado = Cuadrado(50)
print("El area del cuadrado es:", Numlado.area())

##########################################################
lado = int(input("Ingresa el lado?"))
mi_ejemplo = Cuadrado(lado)
r = mi_ejemplo.area()
print(f"El area es {r}")
