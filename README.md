# Grimgar RPG

RPG por turnos jugable desde la terminal, construido para practicar programación orientada a objetos: herencia en tres niveles, clases abstractas, encapsulamiento y separación de responsabilidades.

**Stack:** Python 3.9+ — solo librería estándar (`abc`, `random`). Sin dependencias externas.

---

## Cómo correrlo

```bash
git clone https://github.com/Nishikawaz/1_Basic_RPG.git
cd 1_Basic_RPG
python main.py
```

No hace falta instalar nada ni crear un entorno virtual.

---

## Qué hace

Elegís una clase, le ponés nombre a tu soldado y peleás combates por turnos contra monstruos que se van poniendo más difíciles. El objetivo es sobrevivir hasta el Jefe Oscuro y ganarle.

**Clases jugables**

| Clase | HP | Ataque | Defensa | Particularidad |
|---|---|---|---|---|
| Guerrero | 200 | 35 | 15 | Daño consistente con variación aleatoria de +0 a +10 |
| Ladrón | 100 | 50 | 5 | 50% de crítico a ×2.5 — mucho más frágil, mucho más explosivo |

**Enemigos**

| Monstruo | HP | Ataque | Defensa | Oro | Patrón de ataque |
|---|---|---|---|---|---|
| Goblin | 80 | 20 | 3 | 10 | 30% de chance de atacar dos veces |
| Orco | 160 | 30 | 10 | 25 | Remata (×2 de daño) si el rival baja de 25 HP |
| Jefe Oscuro | 220 | 40 | 15 | 60 | Dos fases: al perder la mitad de su vida se vuelve agresivo y alterna remate y doble ataque |

**Progresión**

- 0–2 victorias → solo Goblin
- 3–4 victorias → Goblin u Orco al azar
- 5+ victorias → aparece el Jefe Oscuro

Vencer al Jefe Oscuro termina la partida con victoria total. Que tu soldado llegue a 0 HP la termina con game over.

**Fórmula de daño:** `max(1, ataque - defensa)`. El mínimo de 1 evita que un rival con mucha defensa se vuelva inmune.

---

## Estructura

```
main.py                          Punto de entrada — solo instancia el Motor
motor.py                         Coordina combates, progresión, oro y estado
ui.py                            Único responsable de prints e inputs
dominio/
├── base/
│   └── personaje.py             Personaje (ABC) — raíz de la jerarquía
└── sub_bases/
    ├── soldado.py               Soldado (ABC) → Guerrero, Ladrón
    └── monstruos.py             Monstruo (ABC) → Goblin, Orco, JefeOscuro
```

---

## Decisiones de diseño

**Jerarquía de tres niveles con abstractas intermedias.** `Personaje` define lo común a todos (HP, defensa, recibir daño). `Soldado` y `Monstruo` son abstractas intermedias que agregan lo propio de cada bando: los soldados llevan contador de victorias, los monstruos llevan recompensa en oro. Recién el tercer nivel es instanciable. Esto evita que un `Goblin` herede un contador de victorias que no usa.

**Patrón *template method* en `Monstruo.atacar()`.** El método `atacar()` está implementado una sola vez en la clase intermedia y resuelve los tres patrones de daño (normal, doble, remate). Cada monstruo concreto solo implementa `decidir_accion()`, que devuelve cuál usar. Agregar un monstruo nuevo es escribir una función de decisión, no reescribir la lógica de combate.

**Encapsulamiento real.** `__hp` y `__max_hp` usan doble guion bajo (*name mangling*) y se exponen solo por `@property` de lectura. La única forma de bajar HP es `recibir_daño()`, que aplica la defensa y hace piso en 0. Nada externo puede asignar HP negativo ni saltearse la defensa.

**El Motor nunca imprime.** Todo `print()` e `input()` vive en `UI`. El Motor le pide a la UI que muestre y le devuelve strings. Cambiar la interfaz a web o a GUI no obligaría a tocar la lógica de juego.

**Estado de vida como propiedad derivada.** No hay un flag `vivo` que haya que mantener sincronizado: `estado` se calcula como `hp > 0`. Un campo menos que puede quedar inconsistente.

---

## Contexto

Challenge de fundamentos de POO. La consigna pedía un juego por consola que demostrara herencia, polimorfismo, clases abstractas y encapsulamiento, sin librerías externas.

El polimorfismo se ve en el loop de combate de `motor.py`: llama a `atacar()` sobre el soldado y sobre el monstruo sin saber de qué clase concreta son. Cada uno resuelve su propio daño y devuelve el mensaje ya formateado.

---

## Limitaciones conocidas

- **El balance está sin ajustar, y el Guerrero es una clase-trampa.** Sobre 20.000 partidas simuladas atacando siempre:

  | Clase | Llega al Jefe Oscuro | Gana la partida | Gana el duelo final a HP completo |
  |---|---:|---:|---:|
  | Guerrero | 99,89% | **0,00%** | 0,11% |
  | Ladrón | 68,62% | 7,91% | 37,95% |

  El Guerrero sobrevive el camino con comodidad y después no puede ganar el duelo final: llega con 84 de 200 HP de mediana, pero incluso a HP completo pierde el 99,89% de las veces. Sus 20–30 de daño por turno necesitan ~9 turnos para bajar al jefe, que lo mata en menos. El Ladrón, más frágil, llega menos veces pero sí puede cerrar. Corregirlo es una decisión de diseño (subir el daño del Guerrero, bajar el HP del jefe, o agregar curación), no un arreglo de código.
- **No hay curación ni items.** El HP no se recupera entre combates, así que la partida es una carrera contra el desgaste. Es lo que hace inviable al Guerrero.
- **El oro se acumula y no se gasta.** Está el contador y la recompensa por monstruo, pero no hay tienda todavía.
- **Huir del combate no tiene costo.** Se puede escapar de cualquier pelea sin penalización, lo que permite evitar todo daño no deseado.
- **Sin tests automatizados.** La verificación fue manual, jugando partidas.
