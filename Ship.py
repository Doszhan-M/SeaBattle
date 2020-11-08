# импорт библтеотек
# импорт классов
from termcolor import colored

from Gamers import *


class PlayerShips(Gamer):
    little_ship = colored('|#|', 'green')
    medium_ship = colored('|#|', 'blue')
    large_ship = colored('|#|', 'yellow')

    # Функция для отрисовки кораблей игрока лекгоко класса, принимает класс корабля и функцию ввода
    def player_little_ship_place(self, ship_class, input_pattern):  # input_pattern = gamer_choice.player_choice
        # При помощи функции eval преобразуем ввод игрока в индексы на игровой доске
        index = self.board_list.index(eval(input_pattern[0]))
        self.board_list[index][input_pattern[1]] = ship_class
        # Создаем кортеж для вычиления след клетки для кораблей классом выше
        temp_value = (index, input_pattern[1])
        self.print_board()
        return temp_value  # возвращает кортеж типа (0, 1)

    # Функция для отрисовки кораблей игрока среднего класса. На вход принимает класс корабля, метод ввода координат
    # игроком класса Gamer.
    def player_medium_ship_place(self, ship_class, input_pattern, port):
        self.player_little_ship_place(ship_class, input_pattern)
        # Присваиваем координаты первой клетки переменной для вычисления вариантов следующего
        temp_value1 = self.player_little_ship_place(ship_class, input_pattern)
        self.access_cell_board = set()
        # Формируем доступные клетки
        temp_value_medium = self.constructor_access_cell(temp_value1, ship_class, port)
        self.flag = 0
        return temp_value_medium

    # Функция для отрисовки кораблей игрока высшего класса. На вход принимает класс корабля, метод ввода координат
    # игроком класса Gamer.
    def player_large_ship_place(self, ship_class, input_pattern, port):
        # Первые две клетки выбираются по приципу корабля среднего класса.Функция вернет значение последнего ввода
        temp_value2 = self.player_medium_ship_place(ship_class, input_pattern, port)
        temp_value_large = self.constructor_access_cell(temp_value2, ship_class, port)
        self.flag = 0
        return temp_value_large

    # Функция для формирования доступных ходов
    def constructor_access_cell(self, temp_value1, ship_class, port):
        try:  # В списке может возникнуть исключение, если игрок выбрал клетку на краю доски
            # Создаем список с соседними клетками
            access_cell = [self.list2[temp_value1[0] + 1] + str(temp_value1[1]),
                           self.list2[abs(temp_value1[0] - 1)] + str(temp_value1[1]),
                           self.list2[temp_value1[0]] + str(temp_value1[1] + 1),
                           self.list2[temp_value1[0]] + str(abs(temp_value1[1] - 1))]
        except (TypeError, IndexError):  # После отвола исключения можно изменить список на более безопасный вариант
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
        self.access_cell_board = self.access_cell_board.union(access_cell)
        print(f'Для расположения крупного корабля, вы должны выбрать только близлежашие клетки' '\n'
              f'Доступные варианты:  {self.access_cell_board}')
        # Поднимаем флаг, чтобы убрать ограничение минимального расстояния между клетками
        self.flag = 1
        if port == 'player':
            temp_value_medium = self.player_little_ship_place(ship_class, self.player_choice())
        else:
            temp_value_medium = self.player_little_ship_place(ship_class, self.computer_choice())
        return temp_value_medium
