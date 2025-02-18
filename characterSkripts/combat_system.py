# combat_system.py
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def shoot(self):
        print(f"{self.name} стреляет, наносит {self.damage} урона")

class Enemy:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Враг убит")
        else:
            print(f"Враг получил {damage} урона, осталось {self.health} здоровья")

class EnemyAI:
    def patrol(self):
        print("Враг патрулирует")

    def react_to_sound(self):
        print("Враг реагирует на звук")

    def attack_player(self):
        print("Враг атакует игрока")