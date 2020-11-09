# импорт библиотек
import random

# импорт классов
from Board import *


class Gamer(Board):
    # Функция ввода координат для игрока для расстановки кораблей
    def player_choice(self):
        input1 = input('Укажите координаты клетки для расположения корабля: ')
        final_value1 = self.choice_constructor(input1, self.player_choice)
        return final_value1  # возвращает кортеж типа (self.a, 1)

    # Функция ввода координат для компьютера
    def computer_choice(self):
        # Ставим соответсвующее значение флага, чтобы программа знала чей ход
        list_computer_step = list(self.list_all_step.difference(self.block_list))
        input1 = random.choice(list_computer_step)
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
    def choice_const(self, input1):
        # Добавляем выбор игрока в список его ходов
        self.step_list.add(input1)
        print('self.step_list-', self.step_list)
        # Вносим координату в блок лист
        self.block_list = self.block_list.union(self.step_list)
        # обрабытываем введенные данные в кортеж, каждый символ отдельно
        input_pattern = 'gamer_board.@'
        input_pattern = input_pattern.replace('@', input1[0])
        number = int(input1[1])
        final_value = (input_pattern, number)
        return final_value  # возвращает кортеж типа (self.a, 1)

    def player_shoot(self, enemy_board):
        input2 = input('Укажите координаты на доске противника: ')
        print('input2', input2)
        print('enemy_board.step_list-', enemy_board.step_list)
        if input2 in enemy_board.step_list:
            if input2 not in self.shoot_list:
                self.shoot_list.add(input2)
                input_pattern = 'enemy_board.@'
                input_pattern = input_pattern.replace('@', input2[0])
                number = int(input2[1])
                final_value = (input_pattern, number)
                print('final_value', final_value)
                return final_value  # возвращает кортеж типа (self.a, 1)






