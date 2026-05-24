# POKE

# Resolución Actividad 1: Clase Pokemon 
## Objetivos 
1. Desarrollar la clase Pokemon.
2. Definir 10 características que posee la clase Pokemon.
3. Definir 3 Acciones que puede realizar la clase Pokemon.
4. Proponer su estructura constructor.
5. Elaborar un diagrama tipo UML inicial de la clase.
6. Los atributos tengan sentido dentro del modelo.
7. Los métodos sean realistas e implementables.

> Cómo cumplimiento de los objetivos se hace entrega del presente documento, donde se trazó todo el curso y puesta en marcha del procedimiento. 
---

## Tabla de contenidos

- [Objetivos](#objetivos)
- [Contextualización](#contextualización)
- [Diseño del sistema](#diseño-del-sistema)
  - [Sistema de combate](#sistema-de-combate)
  - [Gestión de equipos](#gestión-de-equipos)
  - [Entorno de batalla](#entorno-de-batalla)
- [Acciones del Pokemon](#acciones-del-pokemon)
  - [move](#movetarget-pokemon-move_power-float-void)
  - [defend](#defenddamage_received-float-void)
  - [evolve](#evolvenew_level-int-new_ability-str-void)
- [Constructor de la clase Pokemon](#constructor-de-la-clase-pokemon)
- [Diagrama UML](#diagrama-uml)
 

## Objetivos 
1. Modelar un sistema de combate tipo Pokémon usando los términos de Programación Orientada a Objetos aprendidos en clase
2. Definir las clases principales del sistema
3. Diseñar relaciones entre entidades mediante UML
4. Definir atributos y métodos coherentes dentro del modelo
---

## Contextualización

Para dar un buen inicio, es necesario comprender cómo se puede utilizar el concepto de Pokémon y por qué puede abstraerse y relacionarse con la Programación Orientada a Objetos.

Basándonos en la franquicia y en la lógica de los combates de los videojuegos, es posible modelar un sistema donde diferentes entidades interactúan entre sí mediante responsabilidades bien definidas. Esto permite representar mecánicas como combates, efectividad de tipos y gestión de equipos a través de clases, atributos y métodos.

---

## Diseño del sistema

A partir de lo descrito, y basándonos en la franquicia y videojuegos de Pokémon, se propone como parte del diseño la entidad *Pokemon*, integrada dentro de un sistema más amplio, y abstraída con atributos generales como:

- ***Puntos de vida (HP)***: Al ser una entidad viva capacitada para combatir, se utilizan como parámetro de control, el cual cambiará constantemente durante un combate.  
- ***Tipo***: Atributo general que define cómo interactuará un Pokémon en el entorno, determinando sus fortalezas y debilidades frente a otros tipos.  
- ***Nombre***: Identificador único y legible para cada Pokémon.  
- ***Aspecto***: Característica que permite describir visualmente al Pokémon.  
- ***Nivel***: Atributo que influye en el rendimiento general y puede modificarse mediante evolución.  
- ***Habilidad especial***: Capacidad única que puede alterar el comportamiento del Pokémon durante el combate.  
- ***Estadísticas (Stats)***: Conjunto de atributos encapsulados en un objeto que incluye puntos de vida, ataque, defensa, velocidad y ataque especial.  
- ***Movimientos (Moveset)***: Conjunto de acciones que el Pokémon puede ejecutar en combate, limitado a un máximo de cuatro movimientos.  
- ***Etapa de evolución***: Permite rastrear el desarrollo del Pokémon y su progreso dentro del sistema.  

---

### Sistema de combate

- **CombatEngine**: Calcula el daño y determina si un ataque acierta o falla.  
- **TypeRelations**: Define la efectividad entre tipos de Pokémon.  

---

### Gestión de equipos

- **Trainer**: Gestiona un equipo de hasta 6 Pokémon.  
  Permite agregar, seleccionar y cambiar Pokémon durante el combate.  

---

### Entorno de batalla

- **Field**: Controla el combate entre dos Pokémon activos.  
  Gestiona turnos, orden de ataque y ejecución de acciones.  

---

## Acciones del Pokemon

### ***move(target: Pokemon, move_power: float): void***

Acción fundamental para la interacción entre objetos. Permite ejecutar un ataque sobre otro Pokémon, aplicando daño en función del poder del movimiento.

**Parámetros:**
- `target (Pokemon)`: Pokémon que recibirá el ataque  
- `move_power (float)`: Poder base del ataque utilizado  

---

### ***defend(damage_received: float): void***

Permite al Pokémon reducir el daño recibido utilizando sus estadísticas defensivas.

**Parámetros:**
- `damage_received (float)`: Cantidad de daño antes de aplicar la defensa  

---

### ***evolve(new_level: int): void***

Permite al Pokémon aumentar su nivel y evolucionar.

**Parámetros:**
- `new_level (int)`  

---

## Constructor de la clase Pokemon

```python
__init__(
  name: str,
  type: str,
  stats: Stats,
  level: int,
  appearance: str,
  moveset: Moveset,
  special_ability: str
)
```

---

## Diagrama UML
```mermaid
classDiagram
Trainer "1" *-- "1..6" Pokemon : owns and manages
Pokemon "1" *-- "1" Stats
Pokemon "1" *-- "1" Moveset
Moveset "1" o-- "0..4" Move : contains
CombatEngine --> Pokemon
CombatEngine --> Move
CombatEngine --> TypeRelations

class Trainer{
  -name: str
  -team: list[Pokemon]

  +__init__(name: str, team: list[Pokemon])
  +add_pokemon(pokemon: Pokemon)
  +get_active_pokemon() Pokemon
  +switch_pokemon(pokemon_index: int)
}

class Pokemon{
    -name: str
    -type: str
    -stats: Stats
    -level: int
    -appearance: str
    -moveset: Moveset
    -evolution_stage: int

    +__init__(name: str, type: str, stats: Stats, level: int, appearance: str, special_ability: str)
    +move(target: Pokemon, move_power: float) void
    +defend(damage_received: float) void
    +evolve(new_level: int, new_ability: str) void
}

class Stats{
    -hp: int
    -attack: float
    -defense: float
    -speed: int
    -special_attack: float

    +__init__(hp: int, attack: float, defense: float, speed: int, special_attack: float)
}

class Move{
    -name: str
    -type: str
    -power: float
    -accuracy: float
    -pp: int

    +__init__(name: str, type: str, power: float, accuracy: float)
    +calculate_damage() float
}

class Moveset{
    -moves: list[Move]
}

class CombatEngine{
    +calculate_damage(attacker: Pokemon, defender: Pokemon, move: Move) float
    +hit_accuracy(accuracy: float) bool
}

class TypeRelations{
    -type_chart: dict

    +get_effectiveness(attack_type: str, defender_types: list[str]) float
}

Pokemon <|-- FirePokemon
Pokemon <|-- WaterPokemon
Pokemon <|-- GrassPokemon

class FirePokemon{
    -type: str = "fire"

    +__init__(name: str, stats: Stats, level: int, appearance: str, special_ability: str)
}

class WaterPokemon{
    -type: str = "water"

    +__init__(name: str, stats: Stats, level: int, appearance: str, special_ability: str)
}

class GrassPokemon{
    -type: str = "grass"

    +__init__(name: str, stats: Stats, level: int, appearance: str, special_ability: str)
}

Field "1" o-- "2" Pokemon
Field --> CombatEngine

class Field{
    -active_pokemon: list[Pokemon]

    +resolve_turn() void
    +execute_attack() void
}

```
Aunque el sistema puede ampliarse con más características, los componentes descritos representan la estructura fundamental necesaria para modelar un sistema de combate tipo Pokémon utilizando los principios de Programación Orientada a Objetos aprendidos durante las clases.
