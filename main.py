class Pokemon:
    def __init__(self, types: str, name: str, life: int = 10,
                 attack: int = 1, defense: float = 0.5,
                 level: int = 1, special_ability: str = "None"):

        self.types = types
        self.name = name
        self.life = life
        self.attack_power = attack
        self.defense = defense
        self.level = level
        self.special_ability = special_ability

    def attack(self, objective, attack_power):
        damage = attack_power * self.attack_power
        objective.defender(damage)

    def defender(self, damage):
        damage_received = damage * (1 - self.defense)
        self.life -= damage_received

        if self.life < 0:
            self.life = 0

        print(f"{self.name} received {damage_received:.2f} damage. Life: {self.life}")

    def evolucion(self, new_level, new_ability):
        if new_level > self.level:
            self.level = new_level
            self.special_ability = new_ability
            print(f"{self.name} evolved to level {self.level}")
        else:
            print("Cannot evolve to a lower level or the same level.")

class TypeRelations:
    def __init__(self):
        self.diccionario = {
            "Water": {
                "Water": 0.0,
                "Fire": 2.0,
                "Earth": 0.5,
                "Electric": 0.5,
                "Air": 2.0,
                "Steel": 2.0,
                "Grass": 0.5,
                "Poison": 2.0,
            },
            "Fire": {
                "Water": 0.5,
                "Fire": 0.0,
                "Earth": 0.5,
                "Electric": 2.0,
                "Air": 2.0,
                "Steel": 2.0,
                "Grass": 2.0,
                "Poison": 2.0,
            },
            "Earth": {
                "Water": 2.0,
                "Fire": 2.0,
                "Earth": 0.0,
                "Electric": 2.0,
                "Air": 0.5,
                "Steel": 2.0,
                "Grass": 0.5,
                "Poison": 2.0,
            },
            "Electric": {
                "Water": 2.0,
                "Fire": 0.5,
                "Earth": 0.5,
                "Electric": 0.0,
                "Air": 2.0,
                "Steel": 2.0,
                "Grass": 0.5,
                "Poison": 2.0,
            },
            "Air": {
                "Water": 0.5,
                "Fire": 0.5,
                "Earth": 2.0,
                "Electric": 0.5,
                "Air": 0.0,
                "Steel": 0.5,
                "Grass": 2.0,
                "Poison": 2.0,
            },
            "Steel": {
                "Water": 0.5,
                "Fire": 0.5,
                "Earth": 0.5,
                "Electric": 0.5,
                "Air": 2.0,
                "Steel": 0.0,
                "Grass": 2.0,
                "Poison": 2.0,
            },
            "Grass": {
                "Water": 2.0,
                "Fire": 0.5,
                "Earth": 2.0,
                "Electric": 0.5,
                "Air": 0.5,
                "Steel": 0.5,
                "Grass": 0.0,
                "Poison": 0.5,
            },
            "Poison":{
                "Water": 0.5,
                "Fire": 0.5,
                "Earth": 0.5,
                "Electric": 0.5,
                "Air": 0.5,
                "Steel": 0.5,
                "Grass": 2.0,
                "Poison": 0.0,
            }
        }