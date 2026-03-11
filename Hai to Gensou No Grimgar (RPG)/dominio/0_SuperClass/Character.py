from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, nombre, vida, ataque, mana, defensa, velocidad): 
    # Atributos internos protegidos (encapsulados pero solo por convención)
        self.nombre = nombre
        self._stats = {
        "vida" : vida,
        "ataque" : ataque,
        "mana" : mana,
        "defensa" : defensa,
        "velocidad" : velocidad
        }

    # Decorador (encapsulador) que permite la lectura directa de un atributo (Matcheando el nombre del método con el atributo)
    @property # --> Decorador
    def stats(self): # --> Atributo de solo lectura, ya no se llama como función sino que se accede como si fuera una variable.
        return dict(self._stats) # Copia de stats pero con un método que llama a los valores/atributos para evitar modificaciones externas directas.

    # MÉTODOS COMUNES
    def recibir_daño(self, cantidad):
        daño = max(0, cantidad - self._stats["defensa"])
        self._stats["vida"] = max(0, self._stats["vida"] - daño)
        HP = self._stats["vida"]
        print(f"{self.nombre} recibe {daño} de daño.\nSalud restante: {HP}")

    def gastar_mana(self, costo):
        if self._stats["mana"] >= costo:
            self._stats["mana"] -= costo
            return True
        else:
            print("f{self.nombre} no tiene suficiente")
            return False
     
    def curar(self, cantidad):
        self._stats["vida"] += cantidad
        print(f"Te has curado{cantidad} HP. \nTu vida actual es: {self._stats["vida"]}")

    def check_vida(self):
        return self._stats["vida"] > 0
    
    #MÉTODO ABSTRACTO
    def atacar(self, enemigo):
        pass



