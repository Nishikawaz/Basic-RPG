from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, attack, mana, defense, speed): 
    # Atributos internos protegidos (encapsulados pero solo por convención)
        self._name = name
        self._stats = {
        "health" : health,
        "attack" : attack,
        "mana" : mana,
        "defense" : defense,
        "speed" : speed
        }

#Decorador (encapsulador) que permite la lectura directa de un atributo mediante un método (Matcheando el nombre del método con el atributo)
@property
def stats(self):
    return dict(self._stats)
