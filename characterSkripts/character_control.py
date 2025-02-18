# character_control.py
class CharacterMovement:
    """Класс для управления движением персонажа."""
    def run(self):
        """Заставляет персонажа бежать."""
        print("Персонаж бежит")

    def jump(self):
        """Заставляет персонажа прыгать."""
        print("Персонаж прыгает")

    def crouch(self):
        """Заставляет персонажа приседать."""
        print("Персонаж приседает")


class InputHandler:
    """Класс для обработки ввода с клавиатуры и мыши."""
    def handle_keyboard_input(self, key):
        """Обрабатывает ввод с клавиатуры.
        
        Args:
            key (str): Нажатая клавиша.
        """
        print(f"Нажата клавиша: {key}")

    def handle_mouse_input(self, action):
        """Обрабатывает ввод с мыши.
        
        Args:
            action (str): Действие мыши (например, клик).
        """
        print(f"Действие мыши: {action}")


class CharacterAnimation:
    """Класс для управления анимацией персонажа."""
    def walk(self):
        """Запускает анимацию ходьбы."""
        print("Анимация ходьбы")

    def shoot(self):
        """Запускает анимацию стрельбы."""
        print("Анимация стрельбы")

    def reload(self):
        """Запускает анимацию перезарядки."""
        print("Анимация перезарядки")

    def die(self):
        """Запускает анимацию смерти."""
        print("Анимация смерти")