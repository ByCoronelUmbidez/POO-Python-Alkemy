from enum import Enum

class Tipo(Enum):
    V = "Vertebrado"
    I = "Invertebrado"


class Animal: 
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "estoy comiendo"
    
class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "estoy corriendo"
    
class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)

    def volar(self):
        return "estoy volando"

print("------------------------------------------------")    
miGato = Animal(4,Tipo.V)    
print(f"Mi animal tiene {miGato.cantidad_patas} patas")
print(f"Mi animal es {miGato.tipo}")
print(miGato.comer())
print("------------------------------------------------")

miPerro = Perro(4, Tipo.V, "Piru", "Caniche", )
print(f"Mi perro tiene {miPerro.cantidad_patas} patas")
print(f"Mi perro es {miPerro.tipo}")
print(f"Mi perro se llama {miPerro.nombre}")
print(f"Mi perro es de raza {miPerro.raza}")
print(miPerro.correr())
print("------------------------------------------------")

miAguila = Aguila(2, Tipo.V)
print(f"Mi Aguila tiene {miAguila.cantidad_patas} patas")
print(f"Mi Aguila es {miAguila.tipo}")
print(miAguila.volar())
print("------------------------------------------------")