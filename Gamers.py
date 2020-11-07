# импорт библиотек
import random
# импорт классов
from Board import *


class Gamer(Board):

    # Функция ввода координат для игрока для расстановки кораблей
    def player_choice(self):
        input1 = input('Укажите на какое место установить корабль: ')
        final_value1 = self.choice_constructor(input1, self.player_choice)
        return final_value1  # возвращает кортеж типа (self.a, 1)

    # Функция ввода координат для компьютера
    def computer_choice(self):
        list_all_step = list(self.list_all_step)
        input1 = random.choice(list_all_step)
        print('input1', input1)
        final_value = self.choice_constructor(input1, self.computer_choice)
        return final_value  # возвращает кортеж типа (self.a, 1)

    # Функция дополнение для обоих choice, на вход принимает итог от player_choice
    def choice_constructor(self, input1, computer_or_player_choice):
        # Проверка есть ли выбор игрока в возможных вариантах
        if input1 in self.list_all_step:
            # Проверка есть ли выбор игрока в блок листе
            if input1 not in self.block_list:
                self.one_cell_work_list = self.min_distance()  # вызов фунции расчета мин расстояния
                # Проверка есть ли выбор игрока в листе мин расстоянии
                if input1 not in self.one_cell_work_list and self.flag == 0:
                    final_value = self.choice_const(input1)
                    return final_value
                # Проверка есть ли выбор игрока для строение крупных караблей
                elif self.flag == 1:
                    if input1 in self.access_cell_board:
                        final_value = self.choice_const(input1)
                        return final_value
                    else:
                        print('Для расположения крупного корабля, вы должны выбрать только близлежашие клетки Gamer!')
                        return computer_or_player_choice()
                else:
                    print('Расстояние между кораблями должно быть как минимум одна клетка')
                    return computer_or_player_choice()
            else:
                print('Вы не можете выбрать уже занятые квадраты! Выберите другую')
                return computer_or_player_choice()
        else:
            print('Введите клетку из доступных на игровой доске! Например, a1 или c3')
            return computer_or_player_choice()

    # Функция сервис для choice_constructor, на вход принимает ввод игрока ввиде строки
    def choice_const(self, input):
        # Добавляем выбор игрока в список его ходов
        self.player_step_list.add(input)
        # Вносим координату в блок лист
        self.block_list = self.block_list.union(self.player_step_list)
        # обрабытываем введенные данные в кортеж, каждый символ отдельно
        input_pattern = 'self.@'
        input_pattern = input_pattern.replace('@', input[0])
        number = int(input[1])
        final_value = (input_pattern, number)
        return final_value  # возвращает кортеж типа (self.a, 1)
