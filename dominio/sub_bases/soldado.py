# dominio/sub_bases/soldado.py
import random
from abc import abstractmethod
from dominio.base.personaje import Personaje


class Soldado(Personaje):

    def __init__(self, nombre: str, hp: int, ataque: int, defensa: int):
        super().__init__(nombre, hp, ataque, defensa)
        self.__victorias = 0

    @property
    def victorias(self) -> int:
        return self.__victorias

    def registrar_victoria(self) -> None:
        self.__victorias += 1

    @abstractmethod
    def atacar(self, enemigo: Personaje) -> str:
        pass

    @abstractmethod
    def ver_hp(self) -> str:
        pass


class Guerrero(Soldado):

    def __init__(self, nombre: str):
        super().__init__(nombre, hp=200, ataque=35, defensa=15)

    def atacar(self, enemigo: Personaje) -> str:
        daño = self._ataque + random.randint(0, 10)
        real = enemigo.recibir_daño(daño)
        return (f"[Guerrero] {self._nombre} golpea con su espada "
                f"→ {real} de daño a {enemigo.nombre}")

    def ver_hp(self) -> str:
        return (f"Guerrero '{self._nombre}' | HP {self.hp}/{self.max_hp} "
                f"| Victorias {self.victorias}")


class Ladron(Soldado):

    PROB_CRITICO = 0.5
    MULTIPLICADOR_CRITICO = 2.5

    def __init__(self, nombre: str):
        super().__init__(nombre, hp=100, ataque=50, defensa=5)

    def atacar(self, enemigo: Personaje) -> str:
        es_critico = random.random() < self.PROB_CRITICO
        if es_critico:
            daño = int(self._ataque * self.MULTIPLICADOR_CRITICO)
            real = enemigo.recibir_daño(daño)
            return (f"[Ladrón] {self._nombre} encuentra el punto débil "
                    f"→ CRÍTICO {real} de daño a {enemigo.nombre}!")
        real = enemigo.recibir_daño(self._ataque)
        return (f"[Ladrón] {self._nombre} ataca desde las sombras "
                f"→ {real} de daño a {enemigo.nombre}")

    def ver_hp(self) -> str:
        return (f"Ladrón '{self._nombre}' | HP {self.hp}/{self.max_hp} "
                f"| Victorias {self.victorias}")