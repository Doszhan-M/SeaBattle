# импорт библиотек
import random

# импорт классов
from Board import *


class Gamer(Board):

    # Функция ввода координат для игрока для расстановки кораблей
    def player_choice(self):
        input1 = input('Укажите на какое место установить корабль: ')
        final_value = self.choice_constructor(input1)
        return final_value  # возвращает кортеж типа (self.a, 1)

    # Функция ввода координат для компьютера
    def computer_choice(self):
        list_all_step = list(self.list_all_step)
        input1 = random.choice(list_all_step)
        print(input1)
        final_value = self.choice_constructor(input1)
        self.print_board()
        return final_value  # возвращает кортеж типа (self.a, 1)

    def choice_constructor(self, input1):
        # Проверка есть ли выбор игрока в возможных вариантах
        if input1 in self.list_all_step:
            # Проверка есть ли выбор игрока в блок листе
            if input1 not in self.block_list:
                self.min_distance()  # вызов фунции расчета мин расстояния
                # Проверка есть ли выбор игрока в листе мин расстоянии
                if input1 not in self.one_cell_work_list and self.flag == 0:
                    # Добавляем выбор игрока в список его ходов
                    self.player_step_list.add(input1)
                    # Вносим координату в блок лист
                    self.block_list = self.block_list.union(self.player_step_list)
                    # обрабытываем введенные данные в кортеж, каждый символ отдельно
                    input_pattern = 'self.@'
                    input_pattern = input_pattern.replace('@', input1[0])
                    number = int(input1[1])
                    final_value = (input_pattern, number)
                    return final_value  # возвращает кортеж типа (self.a, 1)
                    # Проверка есть ли выбор игрока для строение крупных караблей
                elif self.flag == 1:
                    if input1 in self.access_cell_board:
                        # Добавляем выбор игрока в список его ходов
                        self.player_step_list.add(input1)
                        # Вносим координату в блок лист
                        self.block_list = self.block_list.union(self.player_step_list)
                        # обрабытываем введенные данные в кортеж, каждый символ отдельно
                        input_pattern = 'self.@'
                        input_pattern = input_pattern.replace('@', input1[0])
                        number = int(input1[1])
                        final_value = (input_pattern, number)
                        return final_value  # возвращает кортеж типа (self.a, 1)
                    else:
                        print('Для расположения крупного корабля, вы должны выбрать только близлежашие клетки')
                        return self.player_choice()
                else:
                    print('Расстояние между кораблями должно быть как минимум одна клетка')
                    return self.player_choice()
            else:
                print('Вы не можете выбрать уже занятые квадраты! Выберите другую')
                return self.player_choice()
        else:
            print('Введите клетку из доступных на игровой доске! Например, a1 или c3')
            return self.player_choice()
