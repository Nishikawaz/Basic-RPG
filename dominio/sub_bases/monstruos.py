import random
from abc import abstractmethod
from dominio.base.personaje import Personaje

# Clase intermedia abstracta enemiga
class Monstruo(Personaje):

    def __init__(self, nombre: str, hp: int, ataque: int, defensa: int, recompensa: int):
        super().__init__(nombre, hp, ataque, defensa)
        self.__recompensa = recompensa

    @property
    def recompensa(self) -> int:
        return self.__recompensa

    # Nuevo método abstracto que se implementará desde sub_base a sus objetos
    @abstractmethod
    def decidir_accion(self, enemigo: Personaje) -> str:
        pass

    # Clase abstracta que se bajó de la base
    def atacar(self, enemigo: Personaje) -> str:

        accion = self.decidir_accion(enemigo) # La variable accion indica el tipo de ataque

        if accion == "doble": # Patrón de ataque doble
            real_ataque = enemigo.recibir_daño(self._ataque) # Daño real del ataque
            real_ataque_2 = enemigo.recibir_daño(self._ataque // 2) # Daño real del ataque / 2
            return (f"[Monstruo] {self._nombre} ataca dos veces → {real_ataque} + {real_ataque_2} de daño a {enemigo.nombre}")

        if accion == "rematar": # Patrón de ataque más contundente
            daño = int(self._ataque * 2)
            real = enemigo.recibir_daño(daño)
            return (f"[Monstruo] {self._nombre} va por el remate "
                    f"→ {real} de daño a {enemigo.nombre}!")

        # Daño real del ataque
        real = enemigo.recibir_daño(self._ataque)
        return (f"[Monstruo] {self._nombre} ataca → {real} de daño a {enemigo.nombre}")

    # Otro método abstracto a ser implementado cuando se instancie
    @abstractmethod
    def ver_hp(self) -> str:
        pass

# Mostruo "Goblin" con patrón de ataque doble
class Goblin(Monstruo): 
    def __init__(self):
        super().__init__("Goblin", hp=80, ataque=20, defensa=3, recompensa=10)

    def decidir_accion(self, enemigo: Personaje) -> str:
        # 30% de chances de atacar dos veces
        if random.random() < 0.3:
            return "doble"
        return "atacar"

    def ver_hp(self) -> str:
        return f"Goblin | HP {self.hp}/{self.max_hp}"

# Monstruo "Orco" con patrón de ataque rematar
class Orco(Monstruo):

    def __init__(self):
        super().__init__("Orco", hp=160, ataque=30, defensa=10, recompensa=25)

    def decidir_accion(self, enemigo: Personaje) -> str:
        # Si el enemigo está muy débil, intenta rematarlo
        if enemigo.hp < 25:
            return "rematar"
        # Sino, ataque normal
        return "atacar"

    def ver_hp(self) -> str:
        return f"Orco | HP {self.hp}/{self.max_hp}"

# Monstruo JefeOscuro que ataca adaptándose según el HP
class JefeOscuro(Monstruo):
    
    def __init__(self):
        super().__init__("Jefe Oscuro", hp=220,ataque=40, defensa=15, recompensa=60)
        # Estado interno inicial
        self.__fase = 1

    def decidir_accion(self, enemigo: Personaje) -> str:
        # Activa fase 2 cuando pierde la mitad de su vida
        if self.hp < self.max_hp * 0.5:
            self.__fase = 2

        if self.__fase == 2:
            # Fase 2: más agresivo — prioriza rematar o doble ataque
            if random.random() < 0.5:
                return "rematar"
            return "doble"

        # Fase 1: solo remata si el rival está muy débil
        if enemigo.hp < 30:
            return "rematar"
        return "atacar"

    def ver_hp(self) -> str:
        # Muestra la fase actual para que el jugador sepa que cambió
        return f"Jefe Oscuro [FASE {self.__fase}] | HP {self.hp}/{self.max_hp}"