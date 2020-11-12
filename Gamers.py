# импорт библиотек
import random
import time
# импорт классов
from Board import *


class Gamer(Board):
    # Функция ввода координат для игрока для расстановки кораблей
    def player_choice(self, gamer_board, gamer):
        input1 = input('Укажите координаты для расположения корабля: ')
        final_value1 = self.choice_constructor(input1, self.player_choice, gamer_board, gamer)
        return final_value1  # возвращает кортеж типа (self.a, 1)

    # Функция ввода координат для компьютера
    def computer_choice(self, gamer_board, gamer):
        # Ставим соответсвующее значение флага, чтобы программа знала чей ход
        list_computer_step = list(gamer_board.list_all_step.difference(gamer_board.step_list))
        input1 = random.choice(list_computer_step)
        final_value = self.choice_constructor(input1, self.computer_choice, gamer_board, gamer)
        return final_value  # возвращает кортеж типа (self.a, 1)

    # Функция дополнение для обоих choice, на вход принимает итог от player_choice
    def choice_constructor(self, input1, computer_or_player_choice, gamer_board, gamer):
        # Проверка есть ли выбор игрока в возможных вариантах
        if input1 in gamer_board.list_all_step:
            # Проверка есть ли выбор игрока в блок листе
            if input1 not in gamer_board.step_list:
                gamer_board.one_cell_work_list = gamer_board.min_distance()  # вызов фунции расчета мин расстояния
                # Проверка есть ли выбор игрока в листе мин расстоянии
                if input1 not in gamer_board.one_cell_work_list and gamer_board.flag == 0:
                    final_value = self.choice_const(input1, gamer_board)
                    return final_value
                # Проверка есть ли выбор игрока для строение крупных караблей
                elif gamer_board.flag == 1:
                    if input1 in gamer_board.access_cell_board:
                        final_value = self.choice_const(input1, gamer_board)
                        return final_value
                    elif gamer == 'computer':
                        return computer_or_player_choice(gamer_board, gamer)
                    else:
                        print('Для расположения крупного корабля, вы должны выбрать только близлежашие клетки!')
                        return computer_or_player_choice(gamer_board, gamer)
                else:
                    if gamer == 'player':
                        print('Расстояние между кораблями должно быть как минимум одна клетка')
                    return computer_or_player_choice(gamer_board, gamer)
            else:
                print('Вы не можете выбрать уже занятые квадраты! Выберите другую')
                return computer_or_player_choice(gamer_board, gamer)
        else:
            print('Введите клетку из доступных на игровой доске! Например, f1 или d3')
            return computer_or_player_choice(gamer_board, gamer)

    # Функция сервис для choice_constructor, на вход принимает ввод игрока ввиде строки
    def choice_const(self, input1, gamer_board):
        # Добавляем выбор игрока в список его ходов
        gamer_board.step_list.add(input1)
        # обрабытываем введенные данные в кортеж, каждый символ отдельно
        input_pattern = 'gamer_board.@'
        input_pattern = input_pattern.replace('@', input1[0])
        number = int(input1[1])
        final_value = (input_pattern, number)
        return final_value  # возвращает кортеж типа (self.a, 1)

    # Функция выбора клетки для стрельбы по доске противника. На вход принимает доску противника и свою доску
    def player_shoot(self, gamer_board, enemy_board):
        input2 = input('Укажите координаты на доске противника: ')
        if input2 in gamer_board.list_all_step:
            try:
                if input2 in gamer_board.shoot_list:
                    raise ValueError
            except ValueError:
                print(
                    'raise ValueError: Ранее вы уже открывали огонь по этой точке, следует выбрать другие координаты!')
                return self.player_shoot(gamer_board, enemy_board)
            else:
                return self.shoot_constructor(input2, gamer_board)
        else:
            print('Введите клетку из доступных на игровой доске! Например, f1 или d3')
            return self.player_shoot(gamer_board, enemy_board)

    # Функция выбора клетки для стрельбы по доске противника. На вход принимает доску противника и свою доску
    def computer_shoot(self, gamer_board, enemy_board):
        # Т.к. фунция рандом не перебирает множество делаем из него список
        list_computer_shoot = list(gamer_board.list_all_step.difference(gamer_board.shoot_list))
        input2 = random.choice(list_computer_shoot)
        print(f'Компьютер стреляет по квадрату {input2}')
        time.sleep(2)
        if input2 not in gamer_board.shoot_list:
            return self.shoot_constructor(input2, gamer_board)
        else:
            return self.computer_shoot(gamer_board, enemy_board)

    # Функция конструктор для дальнейшей работы с выбранными клетками. На вход принимает переменные с родителей
    def shoot_constructor(self, input2, gamer_board):
        gamer_board.shoot_list.add(input2)
        input_pattern = 'enemy_board.@'
        input_pattern = input_pattern.replace('@', input2[0])
        number = int(input2[1])
        final_value = (input_pattern, number)
        return final_value  # возвращает кортеж типа (enemy_board.a, 1)
