# импорт классов
from GameLogic import *


class Player(GameLogic):
    # Функция ввода координат для игрока
    def player_choice(self, allow_list):
        input1 = input('Укажите на какое место установить корабль: ')
        if input1 in allow_list:
            self.player_step_list.add(input1)
            input_pattern = 'self.@'
            input_pattern = input_pattern.replace('@', input1[0])
            number = int(input1[1])
            final_value = (input_pattern, number)
            return final_value  # возвращает кортеж типа (self.a, 1)
        else:
            print('Введите клетку из доступных на игровой доскке! Например, a1 или c3')
            return self.player_choice(allow_list)


# Функция ввода координат для компьютера
# def computer_choice(self):