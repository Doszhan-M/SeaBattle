# импорт классов
from Gamers import *


class Ships(Gamer):
    little_ship = colored('|#|', 'green')
    medium_ship = colored('|#|', 'blue')
    large_ship = colored('|#|', 'magenta')
    burning_ship = colored('|X|', 'red')
    miss_ship = colored('|T|', 'cyan')

    # Функция для отрисовки кораблей. Принимает класс корабля, функцию ввода  доски игрока
    @staticmethod
    def ship_place(ship_class, gamer_choice, gamer_board, gamer):
        # При помощи функции eval преобразуем ввод игрока в индексы на игровой доске
        index = gamer_board.board_list.index(eval(gamer_choice[0]))
        gamer_board.board_list[index][gamer_choice[1]] = ship_class
        # Создаем кортеж для вычиления след клетки для кораблей классом выше или для вычисления результатов выстрела
        little_ship_place = (index, gamer_choice[1])
        # Если это ход игрока выводим доску на печать
        if gamer == 'player':
            gamer_board.print_board()
        return little_ship_place  # возвращает кортеж типа (0, 1)

    # Функция для отрисовки кораблей игрока среднего класса. На вход принимает класс корабля, метод ввода координат
    def medium_ship_place(self, ship_class, gamer_choice, gamer_board, gamer):
        # Присваиваем координаты первой клетки переменной для вычисления вариантов следующего
        little_ship_place = self.ship_place(ship_class, gamer_choice, gamer_board, gamer)
        gamer_board.access_cell_board = set()
        # Формируем доступные клетки
        access_cell = self.constructor_medium_ship_access_cell(little_ship_place)
        # Передаем доступные клетки для применения в отрисовке корабля
        medium_ship_place = self.constructor_big_ship_place(access_cell, ship_class, gamer_board, gamer)
        return little_ship_place, medium_ship_place  # возвращает место обеих влеток

    # Функция для отрисовки кораблей игрока высшего класса. На вход принимает класс корабля, метод ввода координат
    def large_ship_place(self, ship_class, gamer_choice, gamer_board, gamer):
        # Первые две клетки выбираются по приципу корабля среднего класса.Функция вернет значение последнего ввода
        medium_ship_place = self.medium_ship_place(ship_class, gamer_choice, gamer_board, gamer)
        # У высшего класса свой конструктор для access list
        access_cell = self.constructor_large_ship_access_cell(medium_ship_place)
        # Передаем доступные клетки для применения в отрисовке корабля
        self.constructor_big_ship_place(access_cell, ship_class, gamer_board, gamer)
        return

        # Функция для формирования доступных ходов среднего корабля

    def constructor_medium_ship_access_cell(self, temp_value_little):
        try:  # В списке может возникнуть исключение, если игрок выбрал клетку на краю доски
            # Создаем список с соседними клетками
            access_cell = [self.list2[temp_value_little[0] + 1] + str(temp_value_little[1]),
                           self.list2[abs(temp_value_little[0] - 1)] + str(temp_value_little[1]),
                           self.list2[temp_value_little[0]] + str(temp_value_little[1] + 1),
                           self.list2[temp_value_little[0]] + str(abs(temp_value_little[1] - 1))]
        except (TypeError, IndexError):  # После отвола исключения можно изменить список на более безопасный вариант
            access_cell = [self.list2[abs(temp_value_little[0] - 1)] + str(temp_value_little[1]),
                           self.list2[temp_value_little[0]] + str(temp_value_little[1] + 1),
                           self.list2[temp_value_little[0]] + str(abs(temp_value_little[1] - 1))]
        return access_cell

    # Функция для формирования доступных ходов высшего корабля
    def constructor_large_ship_access_cell(self, medium_ship_place):
        # даем короткое название для удобной работы
        a = medium_ship_place
        access_cell = []
        if a[0][0] == a[1][0]:
            a1 = self.list2[a[0][0]]
            access_cell = [a1 + str(a[0][1] + 1), a1 + str(a[0][1] - 1), a1 + str(a[1][1] + 1),
                           a1 + str(a[1][1] - 1)]
        elif a[0][1] == a[1][1]:
            a2 = str(a[0][1])
            if min(a[0][0] - 1, a[1][0] - 1) < 0:
                access_cell = [self.list2[a[0][0] + 1] + a2, self.list2[a[1][0] + 1] + a2]
            else:
                try:
                    access_cell = [self.list2[a[0][0] + 1] + a2, self.list2[a[0][0] - 1] + a2,
                                   self.list2[a[1][0] + 1] + a2,
                                   self.list2[a[1][0] - 1] + a2]
                except IndexError:
                    access_cell = [self.list2[a[0][0] - 1] + a2, self.list2[a[1][0] - 1] + a2]
        return access_cell

    # Функция примает на вход резельтаты конструкторов access cell
    def constructor_big_ship_place(self, access_cell, ship_class, gamer_board, gamer):
        # Преобразуем список во множество для логики игры
        access_cell = set(access_cell)
        # Отсекаем невозможные варианты сравнивая с возможными
        access_cell = access_cell.intersection(self.list_all_step)
        # Отсекаем из листа уже выбранные клетки
        access_cell = access_cell.difference(gamer_board.step_list)
        # Добовляем доступные варианты для ограничения выбора
        gamer_board.access_cell_board = gamer_board.access_cell_board.union(access_cell)
        # Вывод делаем только для игрока
        if gamer == 'player':
            print(f'Чтобы продолжить установку крупного корабля, вы должны выбрать только близлежашие клетки.')
            print('Доступные варианты:', colored(gamer_board.access_cell_board, 'red'))
        # Поднимаем флаг, чтобы убрать ограничение минимального расстояния между клетками и наносим корабль
        gamer_board.flag = 1
        if gamer == 'player':
            big_ship_place = self.ship_place(ship_class, self.player_choice(gamer_board, gamer), gamer_board,
                                             gamer)
        else:
            big_ship_place = self.ship_place(ship_class, self.computer_choice(gamer_board, gamer), gamer_board,
                                             gamer)
        gamer_board.flag = 0
        gamer_board.access_cell_board = set()
        return big_ship_place

    # Функция отрисовки корабля после выстрела врага
    def ship_fire(self, gamer_shoot, enemy_board, battle_print_board, gamer, debug):
        # При помощи функции eval преобразуем ввод игрока в индексы на игровой доске
        index = enemy_board.board_list.index(eval(gamer_shoot[0]))
        if gamer_shoot[0][-1] + str(gamer_shoot[-1]) in enemy_board.step_list:
            enemy_board.board_list[index][gamer_shoot[1]] = self.burning_ship
            battle_print_board.board_list[index][gamer_shoot[1]] = self.burning_ship
            if gamer == 'player':
                if debug == 'debug':
                    enemy_board.print_board()
                else:
                    battle_print_board.print_board()
                time.sleep(0.5)
                print(colored('Поподание! Ваш снаряд поразил цель!', 'red'), 'Вы можете выстрелить еще раз.')
                time.sleep(0.5)
            elif gamer == 'computer':
                enemy_board.print_board()
                time.sleep(1.5)
                print(colored('Снаряд компьютера попала по вашему кораблю! Компьютер стреляет еще раз...', 'red'))
                time.sleep(1)
            return self.burning_ship
        else:
            enemy_board.board_list[index][gamer_shoot[1]] = self.miss_ship
            battle_print_board.board_list[index][gamer_shoot[1]] = self.miss_ship
            if gamer == 'player':
                if debug == 'debug':
                    enemy_board.print_board()
                else:
                    battle_print_board.print_board()
                time.sleep(1.5)
                print(colored('Вы промахнулись! Ход переходит компьютеру.', 'blue'))
            elif gamer == 'computer':
                enemy_board.print_board()
                time.sleep(1.5)
                print(colored('Снаряд компьютера пролетел мимо! Ход переходит к вам.', 'green'))
                time.sleep(1)
            return self.miss_ship
