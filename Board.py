# импорт классов
from Gamers import *


class Board(Player):
    # Игровая доска
    w = ['    ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ']
    a = [' a ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    b = [' b ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    c = [' c ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    d = [' d ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    e = [' e ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    f = [' f ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']

    # Вспомогательные переменные для функции интерактива с игроком
    list1 = [a, b, c, d, e, f]
    access_cell_board = set()

    # Функция печати доски
    def print_board(self):
        print(*self.w, '\n', *self.a, '\n', *self.b, '\n', *self.c, '\n', *self.d, '\n', *self.e, '\n', *self.f, '\n',
              '_' * 30)

    # Функция для отрисовки кораблей игрока лекгоко класса
    def player_little_ship_place(self, ship_class, input_pattern):
        index = self.list1.index(eval(input_pattern[0]))
        self.list1[index][input_pattern[1]] = ship_class
        self.print_board()
        self.block_list.update(self.player_step_list)
        temp_value = (index, input_pattern[1])
        return temp_value  # возвращает кортеж типа (0, 1)

    # Функция для отрисовки кораблей игрока среднего класса
    def player_medium_ship_place(self, ship_class, input_pattern):
        self.player_little_ship_place(ship_class, input_pattern)
        self.player_ship_constructor(ship_class, input_pattern)

    # Функция для отрисовки кораблей игрока высшего класса
    def player_large_ship_place(self, ship_class, input_pattern):
        self.player_medium_ship_place(ship_class, input_pattern)
        self.player_ship_constructor(ship_class, input_pattern)

    # Вспомогательная функция для конструктора крупных кораблей
    def player_ship_constructor(self, ship_class, input_pattern):
        temp_value5 = self.player_little_ship_place(ship_class, input_pattern)
        temp_value1 = [temp_value5[0], temp_value5[1]]
        print('Для расположения крупного корабля, вы должны выбрать только близлежашие клетки. ')
        access_cell = [self.list2[temp_value1[0] + 1] + str(temp_value1[1]),
                       self.list2[abs(temp_value1[0] - 1)] + str(temp_value1[1]),
                       self.list2[temp_value1[0]] + str(temp_value1[1] + 1),
                       self.list2[temp_value1[0]] + str(abs(temp_value1[1] - 1))]
        for i in access_cell:
            if '0' in i:
                access_cell.remove(i)
        for i in access_cell:
            if '7' in i:
                access_cell.remove(i)
        access_cell = set(access_cell)
        self.access_cell_board.update(access_cell)
        print(f'Доступные варианты:  {self.access_cell_board}')
        self.player_little_ship_place(ship_class, self.player_choice(self.access_cell_board))
        self.block_list.update(self.player_step_list)
        self.access_cell_board = set()
        return
