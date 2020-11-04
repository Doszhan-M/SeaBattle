from termcolor import colored


class Player:
    # Вспомогательные переменные конструктора доступных вариантов
    list2 = ('a', 'b', 'c', 'd', 'e', 'f')
    list3 = ('1', '2', '3', '4', '5', '6')
    list4 = set()

    # Создаем множество всех доступных вариантов
    def __init__(self):
        for i in self.list2:
            for y in self.list3:
                self.list4.add(i + y)

    # Функция ввода координат клетки на доске
    def player_choice(self, allow_list):
        input1 = input('Укажите на какое место установить корабль: ')
        if input1 in allow_list:
            input_pattern = 'self.@'
            input_pattern = input_pattern.replace('@', input1[0])
            number = int(input1[1])
            final_value = (input_pattern, number)
            return final_value  # возвращает кортеж типа (self.a, 1)
        else:
            print('Введите клетку из доступных на игровой доскке! Например, a1 или c3')
            return self.player_choice(allow_list)


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
        print(self.access_cell_board)
        print(f'Доступные варианты:  {self.access_cell_board}')
        self.player_little_ship_place(ship_class, self.player_choice(self.access_cell_board))
        self.access_cell_board = set()
        return


class Ship:
    ship = colored('|#|', 'green')


ship = Ship()
gamer_board = Board()
player = Player()

count = 0
gamer_board.print_board()
while count < 2:
    gamer_board.player_little_ship_place(ship.ship, player.player_choice(player.list4))
    count += 1
    print(f'Корабль №{count} легкого класса расположен ')
    if count == 1:
        count = 0
        while count < 2:
            gamer_board.player_medium_ship_place(ship.ship, player.player_choice(gamer_board.list4))
            count += 1
            print(f'Корабль №{count} среднего класса расположен ')
            if count == 1:
                count = 0
                while count < 1:
                    gamer_board.player_large_ship_place(ship.ship, player.player_choice(gamer_board.list4))
                    count = 5
                    print(f'Корабль №{count} высшего класса расположен ')


