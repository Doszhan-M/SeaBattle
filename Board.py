# импорт классов
from GameCondition import *


class Board(GameCondition):
    # Игровая доска
    w = ['    ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ']
    a = [' a ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    b = [' b ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    c = [' c ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    d = [' d ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    e = [' e ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
    f = [' f ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']

    # Вспомогательные переменные для функции интерактива с игроком
    board_list = [a, b, c, d, e, f]

    # Функция печати доски
    def print_board(self):
        print(*self.w, '\n', *self.a, '\n', *self.b, '\n', *self.c, '\n', *self.d, '\n', *self.e, '\n', *self.f, '\n',
              '_' * 30)

    # Функция для определения минимальной дистанции между кораблями на игровой доске
    def min_distance(self):
        for i in self.player_step_list:  # a1
            self.one_cell_work_list.add(i.replace(i[1], str(int(i[1]) + 1)))
            self.one_cell_work_list.add(i.replace(i[1], str(int(i[1]) - 1)))
            for y in self.list2:
                if i[0] in y:
                    try:
                        self.one_cell_work_list.add(i.replace(i[0], self.list2[self.list2.index(y) + 1]))
                        self.one_cell_work_list.add(i.replace(i[0], self.list2[abs(self.list2.index(y) - 1)]))
                    except IndexError:
                        self.one_cell_work_list.add(i.replace(i[0], self.list2[abs(self.list2.index(y) - 1)]))
        return self.one_cell_work_list
