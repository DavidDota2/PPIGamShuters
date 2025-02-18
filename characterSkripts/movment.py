# ui.py
class MainMenu:
    def __init__(self):
        self.buttons = ["Новая игра", "Продолжить", "Настройки", "Выход"]

    def display_menu(self):
        print("Главное меню:")
        for button in self.buttons:
            print(f"- {button}")

class HUD:
    def __init__(self):
        self.health = 100
        self.ammo = 30
        self.minimap = "Мини-карта"

    def display_hud(self):
        print(f"Здоровье: {self.health}, Боеприпасы: {self.ammo}, {self.minimap}")

class PauseMenu:
    def __init__(self):
        self.options = ["Сохранить игру", "Настройки", "Вернуться в игру"]

    def display_pause_menu(self):
        print("Меню паузы:")
        for option in self.options:
            print(f"- {option}")