# character_control.py
class CharacterMovement:
    def run(self):
        print("Персонаж бежит")

    def jump(self):
        print("Персонаж прыгает")

    def crouch(self):
        print("Персонаж приседает")

class InputHandler:
    def handle_keyboard_input(self, key):
        print(f"Нажата клавиша: {key}")

    def handle_mouse_input(self, action):
        print(f"Действие мыши: {action}")

class CharacterAnimation:
    def walk(self):
        print("Анимация ходьбы")

    def shoot(self):
        print("Анимация стрельбы")

    def reload(self):
        print("Анимация перезарядки")

    def die(self):
        print("Анимация смерти")