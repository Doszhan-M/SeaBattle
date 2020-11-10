# импорт библиотек
import random

# импорт классов
from Board import *


class Gamer(Board):
    # Функция ввода координат для игрока для расстановки кораблей
    def player_choice(self, gamer_board):
        input1 = input('Укажите координаты клетки для расположения корабля: ')
        final_value1 = self.choice_constructor(input1, self.player_choice, gamer_board)
        return final_value1  # возвращает кортеж типа (self.a, 1)

    # Функция ввода координат для компьютера
    def computer_choice(self, gamer_board):
        # Ставим соответсвующее значение флага, чтобы программа знала чей ход
        list_computer_step = list(self.list_all_step.difference(self.block_list))
        input1 = random.choice(list_computer_step)
        final_value = self.choice_constructor(input1, self.computer_choice, gamer_board)
        return final_value  # возвращает кортеж типа (self.a, 1)

    # Функция дополнение для обоих choice, на вход принимает итог от player_choice
    def choice_constructor(self, input1, computer_or_player_choice, gamer_board):
        # Проверка есть ли выбор игрока в возможных вариантах
        if input1 in self.list_all_step:
            # Проверка есть ли выбор игрока в блок листе
            if input1 not in self.block_list:
                self.one_cell_work_list = self.min_distance()  # вызов фунции расчета мин расстояния
                # Проверка есть ли выбор игрока в листе мин расстоянии
                if input1 not in self.one_cell_work_list and self.flag == 0:
                    final_value = self.choice_const(input1, gamer_board)
                    return final_value
                # Проверка есть ли выбор игрока для строение крупных караблей
                elif self.flag == 1:
                    if input1 in self.access_cell_board:
                        final_value = self.choice_const(input1, gamer_board)
                        return final_value
                    else:
                        print('Для расположения крупного корабля, вы должны выбрать только близлежашие клетки Gamer!')
                        return computer_or_player_choice(gamer_board)
                else:
                    print('Расстояние между кораблями должно быть как минимум одна клетка')
                    return computer_or_player_choice(gamer_board)
            else:
                print('Вы не можете выбрать уже занятые квадраты! Выберите другую')
                return computer_or_player_choice(gamer_board)
        else:
            print('Введите клетку из доступных на игровой доске! Например, a1 или c3')
            return computer_or_player_choice(gamer_board)

    # Функция сервис для choice_constructor, на вход принимает ввод игрока ввиде строки
    def choice_const(self, input1, gamer_board):
        # Добавляем выбор игрока в список его ходов
        gamer_board.step_list.add(input1)
        print('step_list-', gamer_board.step_list)
        # Вносим координату в блок лист
        gamer_board.block_list = gamer_board.block_list.union(gamer_board.step_list)
        print('self.block_list', gamer_board.block_list)
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
            if input2 not in gamer_board.shoot_list:
                print('input2', input2)
                return self.shoot_constructor(input2, gamer_board, enemy_board)
            else:
                print('Введите клетку из доступных на игровой доске! Например, a1 или c3')
                return self.player_shoot(enemy_board, gamer_board)
        else:
            print('Ранее вы уже открывали огонь по этой точке, следует выбрать другие координаты!')
            return self.player_shoot(enemy_board, gamer_board)

    # Функция выбора клетки для стрельбы по доске противника. На вход принимает доску противника и свою доску
    def computer_shoot(self, gamer_board, enemy_board):
        # Т.к. фунция рандом не перебирает множество делаем из него список
        list_computer_shoot = list(gamer_board.list_all_step.difference(gamer_board.shoot_list))
        input2 = random.choice(list_computer_shoot)
        print('input2', input2)
        if input2 not in gamer_board.shoot_list:
            return self.shoot_constructor(input2, gamer_board, enemy_board)
        else:
            print('Ранее вы уже открывали огонь по этой точке, следует выбрать другие координаты!')
            return self.computer_shoot(enemy_board, gamer_board)

    # Функция конструктор для дальнейшей работы с выбранными клетками. На вход принимает переменные с родителей
    def shoot_constructor(self, input2, gamer_board, enemy_board):
        gamer_board.shoot_list.add(input2)
        input_pattern = 'enemy_board.@'
        input_pattern = input_pattern.replace('@', input2[0])
        number = int(input2[1])
        final_value = (input_pattern, number)
        print('final_value', final_value)
        return final_value  # возвращает кортеж типа (enemy_board.a, 1)


