# combat_system.py
class Weapon:
    """Класс для управления оружием."""
    def __init__(self, name, damage):
        """Инициализация оружия.
        
        Args:
            name (str): Название оружия.
            damage (int): Урон, наносимый оружием.
        """
        self.name = name
        self.damage = damage

    def shoot(self):
        """Запускает стрельбу из оружия."""
        print(f"{self.name} стреляет, наносит {self.damage} урона")


class Enemy:
    """Класс для управления врагами."""
    def __init__(self, health):
        """Инициализация врага.
        
        Args:
            health (int): Здоровье врага.
        """
        self.health = health

    def take_damage(self, damage):
        """Наносит урон врагу.
        
        Args:
            damage (int): Количество урона.
        """
        self.health -= damage
        if self.health <= 0:
            print("Враг убит")
        else:
            print(f"Враг получил {damage} урона, осталось {self.health} здоровья")


class EnemyAI:
    """Класс для управления искусственным интеллектом врагов."""
    def patrol(self):
        """Заставляет врага патрулировать."""
        print("Враг патрулирует")

    def react_to_sound(self):
        """Заставляет врага реагировать на звук."""
        print("Враг реагирует на звук")

    def attack_player(self):
        """Заставляет врага атаковать игрока."""
        print("Враг атакует игрока")