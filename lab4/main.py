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


# Объект для хранения переназначаемых действий
key_actions = {
  'A': lambda: print('Вы нажали A'),
  'B': lambda: print('Вы нажали B'),
  'C': lambda: print('Вы нажали C'),
  'D': lambda: print('Вы нажали D'),
  'E': lambda: print('Вы нажали E'),
  'F': lambda: print('Вы нажали F'),
  'ctrl+c': lambda: print('Вы нажали Ctrl+C'),
  'ctrl+v': lambda: print('Вы нажали Ctrl+V'),
}

# Стек для хранения истории действий
action_history = []

# Функция для нажатия клавиши
def press_key(key):
  if key in key_actions:
    key_actions[key]()
    action_history.append(key)

# Функция для отката действий
def undo_last_action():
  if action_history:
    last_action = action_history.pop()
    print('Отменено действие: ' + last_action)


# Функция для симуляции нажатия клавиши
def simulate_key_press(key):
  press_key(key)
  time.sleep(1)

# Симуляция последовательности нажатий клавиш
simulate_key_press('A') # нажать 'A' 
simulate_key_press('B') # нажать 'B'
undo_last_action() # отменить последнее действие

# Переназначение действия для клавиши 'A'
key_actions['A'] = lambda: print('Переназначено: теперь вы нажали A')
key_actions['C'] = lambda: print('Переназначено: теперь вы нажали C')
key_actions['E'] = lambda: print('Переназначено: теперь вы нажали E')
key_actions['ctrl+c'] = lambda: print('Переназначено: теперь вы нажали Ctrl+C')

# Сброс истории действий
action_history = []

# Перезапуск workflow
simulate_key_press('A') # нажать 'A' 
simulate_key_press('B') # нажать 'B'
simulate_key_press('C') # нажать 'C'
simulate_key_press('D') # нажать 'D'
simulate_key_press('E') # нажать 'E'
press_key('ctrl+c') # нажать 'ctrl+c'
press_key('ctrl+v') # нажать 'ctrl+v'
simulate_key_press('F') # нажать 'F'
undo_last_action() # отменить последнее действие
undo_last_action() # отменить последнее действие
