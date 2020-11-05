# импорт библтеотек
from termcolor import colored

# импорт классов
from Gamers import *


class PlayerShips(Player):
    little_ship = colored('|#|', 'green')
    medium_ship = colored('|#|', 'blue')
    large_ship = colored('|#|', 'yellow')

    # Функция для отрисовки кораблей игрока лекгоко класса
    def player_little_ship_place(self, ship_class, input_pattern):
        # При помощи функции eval преобразуем ввод игрока в индексы на игровой доске
        index = self.board_list.index(eval(input_pattern[0]))
        self.board_list[index][input_pattern[1]] = ship_class
        self.print_board()
        # Создаем кортеж для вычиления след клетки для кораблей классом выше
        temp_value = (index, input_pattern[1])
        return temp_value  # возвращает кортеж типа (0, 1)

    # Функция для отрисовки кораблей игрока среднего класса
    def player_medium_ship_place(self, ship_class, input_pattern):
        # Первая клетка выбирается по приципу корабля легкого класса
        self.player_little_ship_place(ship_class, input_pattern)
        # Присваиваем координаты первой клетки переменной для вычисления вариантов следующего
        temp_value1 = self.player_little_ship_place(ship_class, input_pattern)
        try:  # В списке может возникнуть исключение, если игрок выбрал клетку на краю доски
            # Создаем список с соседники клетками
            access_cell = [self.list2[temp_value1[0] + 1] + str(temp_value1[1]),
                           self.list2[abs(temp_value1[0] - 1)] + str(temp_value1[1]),
                           self.list2[temp_value1[0]] + str(temp_value1[1] + 1),
                           self.list2[temp_value1[0]] + str(abs(temp_value1[1] - 1))]
        except TypeError:  # После отвола исключения можно изменить список на более безопасный вариант
            access_cell = [self.list2[abs(temp_value1[0] - 1)] + str(temp_value1[1]),
                           self.list2[temp_value1[0]] + str(temp_value1[1] + 1),
                           self.list2[temp_value1[0]] + str(abs(temp_value1[1] - 1))]
        # убираем из списка ненужные клетки
        for i in access_cell:
            if '0' in i:
                access_cell.remove(i)
        for i in access_cell:
            if '7' in i:
                access_cell.remove(i)
        # Преобразуем список во множество для логики игры
        access_cell = set(access_cell)
        # Добовляем доступные варианты для ограничения выбора
        self.access_cell_board = set()
        self.access_cell_board = self.access_cell_board.union(access_cell)
        print(f'Для расположения крупного корабля, вы должны выбрать только близлежашие клетки' '\n'
              f'Доступные варианты:  {self.access_cell_board}')
        self.flag = 1
        self.player_little_ship_place(ship_class, self.player_choice())
        self.flag = 0
        self.access_cell_board = set()
        self.access_cell_board = self.access_cell_board.union(self.list_all_step)
        return

    # Функция для отрисовки кораблей игрока высшего класса
    def player_large_ship_place(self, ship_class, input_pattern):
        # Первая две клетки выбираются по приципу корабля среднего класса
        self.player_medium_ship_place(ship_class, input_pattern)
