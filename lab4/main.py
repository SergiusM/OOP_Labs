"""
1) Создать виртуальную
клавиатуру с
переназначаемыми действиями
для
клавиш, с возможностью отката
действий назад.

2) Продемонстрировать работу
клавиатуры сделал workflow из
нажатий различных комбинаций
клавиш и откатов назад.
'Симулировать демонстрацию.
нажатий клавиш путем вывода
значения в консоль и задержкой
между нажатиями

3) Продемонстрировать
переназначение клавиши и
комбинации клавиш с
перезапуком workflow
"""
import time

class Keyboard:
    def __init__(self):
        self.keymap = {}
        self.history = []

    def register_key(self, key, action, undo_action):
        self.keymap[key] = (action, undo_action)

    def press_key(self, key):
        if key not in self.keymap:
            raise Exception("Неизвестная клавиша нажата")
        self.history.append(key)
        self.keymap[key][0]()

    def undo(self):
        if self.history:
            self.keymap[self.history[-1]][1]()
            self.history.pop()

    def is_key_registered(self, key):
        return key in self.keymap


class Workflow:
    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.actions = []

    def keypress(self, key):
        self.keyboard.press_key(key)
        time.sleep(1)

    def undo(self):
        self.keyboard.undo()
        time.sleep(1)

    def perform(self):
        for action in self.actions:
            action()
            time.sleep(1)

    def add_action(self, action):
        self.actions.append(action)


def main():
    keyboard = Keyboard()
    keyboard.register_key("A", lambda: print("Клавиша A нажата"), lambda: None)
    keyboard.register_key("Ctrl+C", lambda: print("Комбинация Ctrl+C нажата"), lambda: print("Ctrl+C action undone"))
    keyboard.register_key("Ctrl+V", lambda: print("Комбинация Ctrl+V нажата"), lambda: print("Ctrl+V action undone"))
    keyboard.register_key("F1", lambda: print("F1 нажата"), lambda: None)
    keyboard.register_key("F2", lambda: print("F2 нажата"), lambda: None)

    
    workflow = Workflow(keyboard)
    workflow.add_action(lambda: workflow.keypress("A"))
    workflow.add_action(lambda: workflow.keypress("Ctrl+C"))
    workflow.add_action(lambda: workflow.keypress("Ctrl+V"))
    workflow.add_action(lambda: workflow.keypress("F1")) 
    workflow.add_action(lambda: workflow.keypress("F2")) 
    workflow.add_action(lambda: workflow.undo())
    workflow.add_action(lambda: workflow.undo())

    workflow.perform()

    print("\nПереназначение клавиш и перезапуск процесса...")
    keyboard.register_key("A", lambda: print("Клавиша A теперь ничего не делает"), lambda: None)
    keyboard.register_key("Ctrl+C", lambda: print("Комбинация Ctrl+C теперь выводит 87 "), lambda: print("Undo action for Ctrl+C"))
    keyboard.register_key("Ctrl+V", lambda: print("Комбинация Ctrl+V теперь выводит 1"), lambda: print("Undo action for Ctrl+V"))

    workflow.perform()

    if keyboard.is_key_registered("Ctrl+V"):
        print("Клавиша Ctrl+V зарегистрирована в системе")

if __name__ == '__main__':
    main()
