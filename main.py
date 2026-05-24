import random
import time  # noqa: I001
from typing import List


class TypeRelations:
    def __init__(self) -> None:
        self.type_chart: dict[str, dict[str, float]] = {
            "Fire": {
                "Fire": 0.5,
                "Water": 0.5,
                "Grass": 2.0,
                "Electric": 1.0,
                "Ground": 1.0,
            },
            "Water": {
                "Fire": 2.0,
                "Water": 0.5,
                "Grass": 0.5,
                "Electric": 1.0,
                "Ground": 2.0,
            },
            "Grass": {
                "Fire": 0.5,
                "Water": 2.0,
                "Grass": 0.5,
                "Electric": 1.0,
                "Ground": 2.0,
            },
            "Electric": {
                "Fire": 1.0,
                "Water": 2.0,
                "Grass": 0.5,
                "Electric": 0.5,
                "Ground": 0.0,
            },
            "Ground": {
                "Fire": 2.0,
                "Water": 1.0,
                "Grass": 0.5,
                "Electric": 2.0,
                "Ground": 1.0,
            },
        }

    def get_effectiveness(self, attack_type: str, defender_types: List[str]) -> float:
        multiplier: float = 1.0

        for defender in defender_types:
            if attack_type in self.type_chart:
                if defender in self.type_chart[attack_type]:
                    multiplier = multiplier * self.type_chart[attack_type][defender]
                else:
                    multiplier = multiplier * 1.0
            else:
                multiplier = multiplier * 1.0

        return multiplier


class Stats:
    def __init__(
        self,
        hp: float,
        attack: float,
        defense: float,
        special_attack: float,
        special_defense: float,
        speed: float,
    ):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self):
        return (
            f"HP: {self.hp}, ",
            f"Attack: {self.attack}, Defense: {self.defense}, "
            f"Sp. Attack: {self.special_attack}, Sp. Defense: {self.special_defense}, ",
            f"Speed: {self.speed}",
        )


class Move:
    def __init__(self, name: str, type: str, power: float, accuracy: int, pp: int):
        self._name = name
        self._type = type
        self._power = power
        self._accuracy = accuracy
        self._pp = pp

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type

    @property
    def power(self) -> float:
        return self._power

    @property
    def accuracy(self) -> int:
        return self._accuracy

    @property
    def pp(self) -> int:
        return self._pp


class Moveset:
    def __init__(self, moves: List[Move] | None = None):
        self.moves: List[Move] = []
        if moves:
            for move in moves:
                self.add_move(move)

    def add_move(self, move: Move) -> bool:
        if len(self.moves) < 4:
            self.moves.append(move)
            print(f"¡El Pokémon aprendió {move.name}!")
            time.sleep(0.5)
            return True
        else:
            print(f"El Pokémon intenta aprender {move.name}, pero tiene 4 movimientos.")
            time.sleep(0.5)
            return False

    def remove_move(self, index: int) -> bool:
        if 0 <= index < len(self.moves):
            removed_move = self.moves.pop(index)
            print("1, 2 y... ¡Poof!")
            time.sleep(1)
            print(f"El Pokémon olvidó cómo usar {removed_move.name}.")
            time.sleep(0.5)
            return True
        else:
            print("Índice no válido. No se pudo olvidar el movimiento.")
            return False

    def replace_move(self, index: int, new_move: Move) -> bool:
        if 0 <= index < len(self.moves):
            old_move = self.moves[index]
            print("1, 2 y... ¡Poof!")
            time.sleep(1)
            print(f"El Pokémon olvidó cómo usar {old_move.name} y...")
            time.sleep(1)
            self.moves[index] = new_move
            print(f"¡Aprendió {new_move.name}!")
            time.sleep(0.5)
            return True
        else:
            print("Índice no válido. No se pudo reemplazar el movimiento.")
            return False

    def get_moves(self) -> List[Move]:
        return self.moves

    def show_moves(self) -> None:
        if not self.moves:
            print("El Pokémon aún no conoce ningún movimiento.")
            time.sleep(0.5)
        else:
            print("\n" + "=" * 45)
            print("                 MOVIMIENTOS")
            print("=" * 45)
            for i, move in enumerate(self.moves):
                print(
                    f"[{i + 1}] {move.name.ljust(12)} | Tipo: {move.type.ljust(8)}"
                    f"| Poder: {str(move.power).ljust(3)} | PP: {move.pp}"
                )
            print("=" * 45 + "\n")
            time.sleep(0.5)


class Pokemon:
    def __init__(self, tipo: str, nombre: str, vida: int = 10,
                 ataque: int = 1, defensa: float = 0.5,
                 nivel: int = 1, habilidad_especial: str = "ninguno"):

        self.tipo = tipo
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.habilidad_especial = habilidad_especial

    def attack(self, target, attack_power):
        damage = attack_power * self.ataque
        target.defender(damage)

    def defender(self, damage):
        reduced_damage = damage * (1 - self.defensa)
        self.vida -= reduced_damage

        if self.life < 0:
            self.life = 0

        print(f"{self.nombre} recibió {reduced_damage:.2f} de daño. Vida: {self.vida}")

    def evolucion(self, nuevo_nivel, nueva_habilidad):
        if nuevo_nivel > self.nivel:
            self.nivel = nuevo_nivel
            self.habilidad_especial = nueva_habilidad
            print(f"{self.nombre} evolucionó al nivel {self.nivel}")
        else:
            print("No puede evolucionar a un nivel menor")