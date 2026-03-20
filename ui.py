# Única responsable de prints e inputs, el Motor nunca realiza prints directamente.
class UI:
    # Intro del juego
    def mostrar_intro(self) -> None:
        print("\n" + "═" * 45)
        print("           GRIMGAR RPG")
        print("   Sobreviví en un mundo que no conocés.")
        print("═" * 45)

    def mostrar_estado(self, soldado, oro: int, victorias: int) -> None:
        print(f"\n{'─' * 45}")
        print(f"  {soldado.ver_hp()}")
        print(f"  Oro: {oro} | Victorias: {victorias}")
        print(f"{'─' * 45}")

    def mostrar_ficha(self, soldado) -> None:
        print(f"\n--- Ficha de {soldado.nombre} ---")
        print(f"  {soldado.ver_hp()}")

    def mostrar_clases(self) -> None:
        print("\nElegí tu clase:")
        print("  1. Guerrero — 200 HP | daño físico consistente")
        print("  2. Ladrón   — 100 HP  | críticos devastadores")

    # En el menú
    def mostrar_menu_principal(self) -> str:
        print("\n¿Qué hacés?")
        print("  1. Ir a combate")
        print("  2. Ver ficha")
        print("  3. Salir")
        return self.pedir_opcion(["1", "2", "3"])

    def mostrar_menu_combate(self) -> str:
        print("\n  Tu turno:")
        print("    1. Atacar")
        print("    2. Huir")
        return self.pedir_opcion(["1", "2"])

    # Durante el combate
    def mostrar_inicio_combate(self, soldado, monstruo) -> None:
        print(f"\n{'═' * 45}")
        print(f"  {soldado.nombre}  VS  {monstruo.nombre}")
        print(f"{'═' * 45}")

    def mostrar_turno(self, turno: int, soldado, monstruo) -> None:
        print(f"\n  Turno {turno}")
        print(f"  {soldado.ver_hp()}")
        print(f"  {monstruo.ver_hp()}")

    def mostrar_victoria_combate(self, soldado, monstruo,
                                  recompensa: int) -> None:
        print(f"\n{'═' * 45}")
        print(f"  VICTORIA — {soldado.nombre} venció a {monstruo.nombre}")
        print(f"  +{recompensa} de oro ganado")
        print(f"{'═' * 45}")

    def mostrar_derrota_combate(self, soldado, monstruo) -> None:
        print(f"\n{'═' * 45}")
        print(f"  DERROTA — {soldado.nombre} fue vencido por {monstruo.nombre}")
        print(f"{'═' * 45}")

    # Fin del juego
    def mostrar_derrota(self, soldado) -> None:
        print("\n" + "═" * 45)
        print("  GAME OVER")
        print(f"  {soldado.nombre} cayó en Grimgar.")
        print("═" * 45)

    # Pantalla final — solo se muestra al vencer al JefeOscuro
    def mostrar_victoria_total(self, soldado, oro: int) -> None:
        print("\n" + "═" * 45)
        print("  VICTORIA TOTAL")
        print(f"  {soldado.nombre} derrotó al Jefe Oscuro.")
        print(f"  Oro acumulado: {oro}")
        print(f"  Victorias: {soldado.victorias}")
        print("═" * 45)

    # Inputs y utilidades
    def pedir_nombre(self, prompt: str = "Nombre") -> str:
        valor = input(f"\n{prompt}: ").strip()
        return valor if valor else "Anónimo"

    def pedir_opcion(self, validas: list[str]) -> str:
        while True:
            opcion = input("  Opción: ").strip()
            if opcion in validas:
                return opcion
            print(f"  Opción inválida. Elegí entre: {validas}")

    def mostrar_mensaje(self, msg: str) -> None:
        print(msg)

    def pausa(self) -> None:
        input("\n  [Enter para continuar]")