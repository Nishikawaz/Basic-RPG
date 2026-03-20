# motor.py
import random
from dominio import (
    Guerrero, Ladron, # Los objetos de la sub_base "Soldado"
    Goblin, Orco, JefeOscuro # Los objetos de la sub_base "Monstruo"
)
from ui import UI # Import de los métodos para mostrar

# Motor del juego. Coordina los combates, estados y la progresión.
class Motor:
    def __init__(self):
        self._ui = UI()             # Única instancia de UI
        self._soldado = None        # Asignación al elegir
        self._oro = 0               # Recompensa acumulada
        self._victorias = 0         # Contador global de combates ganados
        self._ejecutando = False    # Control del loop principal

    # Punto de entrada / LOOP PRINCIPAL
    def iniciar(self) -> None:
        self._ui.mostrar_intro()
        self._elegir_soldado()
        self._ejecutando = True

        # Muestra el estado actual antes de cada decisión
        while self._ejecutando:
            self._ui.mostrar_estado(self._soldado, self._oro, self._victorias)
            opcion = self._ui.mostrar_menu_principal()

            if opcion == "1":
                self._iniciar_combate()
            elif opcion == "2":
                self._ui.mostrar_ficha(self._soldado)
            elif opcion == "3": # Indica si se sigue jugando
                self._ejecutando = False

            # Verifica si el soldado sigue vivo
            if not self._soldado.estado:
                self._ui.mostrar_derrota(self._soldado)
                self._ejecutando = False

    # Setup inicial
    def _elegir_soldado(self) -> None:
        self._ui.mostrar_clases()
        opcion = self._ui.pedir_opcion(["1", "2"])
        nombre = self._ui.pedir_nombre("Nombre de tu soldado")

        if opcion == "1":
            self._soldado = Guerrero(nombre)
        else:
            self._soldado = Ladron(nombre)

        self._ui.mostrar_mensaje(
            f"\n{nombre} se une a los soldados voluntarios de Grimgar.\n"
        )

    # Combate
    def _iniciar_combate(self) -> None:
        monstruo = self._generar_monstruo()
        self._ui.mostrar_inicio_combate(self._soldado, monstruo)
        self._loop_combate(monstruo)                                # Inicio del combate

    def _loop_combate(self, monstruo) -> None:
        turno = 1

        while self._soldado.estado and monstruo.estado:
            self._ui.mostrar_turno(turno, self._soldado, monstruo)

            accion = self._ui.mostrar_menu_combate()

            if accion == "1":
                msg = self._soldado.atacar(monstruo)
                self._ui.mostrar_mensaje(f"  {msg}")
            elif accion == "2":
                self._ui.mostrar_mensaje(
                    f"\n  {self._soldado.nombre} huye del combate."
                )
                return

            if not monstruo.estado:
                break

            msg = monstruo.atacar(self._soldado)
            self._ui.mostrar_mensaje(f"  {msg}")

            turno += 1
            self._ui.pausa()

        self._resolver_combate(monstruo)

    def _resolver_combate(self, monstruo) -> None:
        if self._soldado.estado:
            self._oro += monstruo.recompensa
            self._soldado.registrar_victoria()
            self._victorias += 1
            self._ui.mostrar_victoria_combate(
                self._soldado, monstruo, monstruo.recompensa
            )
        else:
            self._ui.mostrar_derrota_combate(self._soldado, monstruo)

    # Generación de monstruos
    def _generar_monstruo(self):
        if self._victorias >= 5:
            return JefeOscuro()
        if self._victorias >= 3:
            return random.choice([Orco, Goblin])()
        return Goblin()