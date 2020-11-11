# импорт библтеотек
from termcolor import colored

# импорт классов
from Gamers import *


class Ships(Gamer):
    little_ship = colored('|#|', 'green')
    medium_ship = colored('|#|', 'magenta')
    large_ship = colored('|#|', 'blue')
    burning_ship = colored('|X|', 'red')
    miss_ship = colored('|T|', 'cyan')

    # Функция для отрисовки кораблей либо результата выстрела. Принимает класс корабля, функцию ввода  доски игрока
    def ship_place(self, ship_class, gamer_choice, gamer_board, gamer):
        # При помощи функции eval преобразуем ввод игрока в индексы на игровой доске
        index = gamer_board.board_list.index(eval(gamer_choice[0]))
        gamer_board.board_list[index][gamer_choice[1]] = ship_class
        # Создаем кортеж для вычиления след клетки для кораблей классом выше или для вычисления результатов выстрела
        temp_value = (index, gamer_choice[1])
        # Если это ход игрока выводим доску на печать
        if gamer == 'player':
            gamer_board.print_board()
        return temp_value  # возвращает кортеж типа (0, 1)

    # Функция для отрисовки кораблей игрока среднего класса. На вход принимает класс корабля, метод ввода координат
    # игроком класса Gamer.
    def medium_ship_place(self, ship_class, gamer_choice, gamer_board, gamer):
        self.ship_place(ship_class, gamer_choice, gamer_board, gamer)
        # Присваиваем координаты первой клетки переменной для вычисления вариантов следующего
        temp_value1 = self.ship_place(ship_class, gamer_choice, gamer_board, gamer)
        gamer_board.access_cell_board = set()
        # Формируем доступные клетки
        temp_value_medium = self.constructor_access_cell(temp_value1, ship_class, gamer_board, gamer)
        gamer_board.flag = 0
        return temp_value_medium

    # Функция для отрисовки кораблей игрока высшего класса. На вход принимает класс корабля, метод ввода координат
    # игроком класса Gamer.
    def large_ship_place(self, ship_class, gamer_choice, gamer_board, gamer):
        # Первые две клетки выбираются по приципу корабля среднего класса.Функция вернет значение последнего ввода
        temp_value2 = self.ship_place(ship_class, gamer_choice, gamer_board, gamer)
        temp_value_large = self.constructor_access_cell(temp_value2, ship_class, gamer_board, gamer)
        gamer_board.flag = 0
        return temp_value_large

    # Функция для формирования доступных ходов
    def constructor_access_cell(self, temp_value1, ship_class, gamer_board, gamer):
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
        gamer_board.access_cell_board = gamer_board.access_cell_board.union(access_cell)
        print(f'Для расположения крупного корабля, вы должны выбрать только близлежашие клетки' '\n'
              f'Доступные варианты:  {gamer_board.access_cell_board}')
        # Поднимаем флаг, чтобы убрать ограничение минимального расстояния между клетками
        gamer_board.flag = 1
        if gamer == 'player':
            temp_value_medium = self.ship_place(ship_class, self.player_choice(gamer_board), gamer_board,
                                                          gamer)
        else:
            temp_value_medium = self.ship_place(ship_class, self.computer_choice(gamer_board), gamer_board,
                                                          gamer)
        return temp_value_medium

    # Функция отправки результата стрельбы по кораблю
    def ship_fire(self, gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer):
        # При помощи функции eval преобразуем ввод игрока в индексы на игровой доске
        index = enemy_board.board_list.index(eval(gamer_shoot[0]))
        if gamer_shoot[0][-1] + str(gamer_shoot[-1]) in enemy_board.step_list:
            enemy_board.board_list[index][gamer_shoot[1]] = self.burning_ship
            battle_print_board.board_list[index][gamer_shoot[1]] = self.burning_ship
            battle_print_board.print_board()
            return self.burning_ship
        else:
            enemy_board.board_list[index][gamer_shoot[1]] = self.miss_ship
            battle_print_board.board_list[index][gamer_shoot[1]] = self.miss_ship
            battle_print_board.print_board()
            if gamer == 'player':
                print('Вы промахнулись! Ход переходит компьютеру. Компьютер - ')
            if gamer == 'computer':
                print('Снаряд компьютера попал мимо! Ход переходит вам. Уважаемый игрок - ')
            return self.miss_ship
