from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre:str, hp:int, ataque:int, defensa:int):
        self._nombre = nombre
        self.__hp = hp
        self.__max_hp = hp
        self._ataque = ataque
        self._defensa = defensa

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def hp(self) -> int:
        return self.__hp
    
    @property
    def max_hp(self) -> int:
        return self.__max_hp
    
    @property
    def estado(self) -> bool:
        return self.__hp > 0
    
    def recibir_daño(self, cantidad:int) -> int:
        daño_real = max(1, cantidad - self._defensa)
        self.__hp = max(0, self.__hp - daño_real)
        return daño_real
    
    @abstractmethod
    def atacar(self, enemigo: "Personaje") -> str:
        pass

    @abstractmethod
    def ver_hp(self) -> str:
        pass