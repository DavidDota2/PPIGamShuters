# ui.py
class MainMenu:
    """Класс для управления главным меню игры."""
    def __init__(self):
        """Инициализация кнопок главного меню."""
        self.buttons = ["Новая игра", "Продолжить", "Настройки", "Выход"]

    def display_menu(self):
        """Отображает главное меню с доступными кнопками."""
        print("Главное меню:")
        for button in self.buttons:
            print(f"- {button}")


class HUD:
    """Класс для отображения HUD (интерфейса в игре)."""
    def __init__(self):
        """Инициализация параметров HUD: здоровье, боеприпасы, мини-карта."""
        self.health = 100
        self.ammo = 30
        self.minimap = "Мини-карта"

    def display_hud(self):
        """Отображает текущее состояние HUD."""
        print(f"Здоровье: {self.health}, Боеприпасы: {self.ammo}, {self.minimap}")


class PauseMenu:
    """Класс для управления меню паузы."""
    def __init__(self):
        """Инициализация опций меню паузы."""
        self.options = ["Сохранить игру", "Настройки", "Вернуться в игру"]

    def display_pause_menu(self):
        """Отображает меню паузы с доступными опциями."""
        print("Меню паузы:")
        for option in self.options:
            print(f"- {option}")