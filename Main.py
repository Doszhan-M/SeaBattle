class Board:
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
    number = 0

    # Функция печати доски
    def print_board(self):
        print(*self.w, '\n', *self.a, '\n', *self.b, '\n', *self.c, '\n', *self.d, '\n', *self.e, '\n', *self.f, '\n', '_' * 30)

    # Функция ввода координат клетки на доске
    def player_choice(self):
        self.print_board()
        input1 = 'a4'# input('mumber ship: ')
        # input_pattern = 'self.$[@]'
        # input_pattern = input_pattern.replace('$', input1[0])
        # input_pattern = input_pattern.replace('@', input1[1])
        input_pattern = 'self.@'
        input_pattern = input_pattern.replace('@', input1[0])
        self.number = int(input1[1])
        return input_pattern

    # Функция отрисовки кораблей игрока
    def player_ship_place(self, ship_class):
       # self.player_choice()
        index = self.list1.index(eval(self.player_choice()))
        print(index)
        self.list1[index][self.number] = ship_class


class Ship:
    little_ship = '|#|'
    medium_ship = '|#|'


ship = Ship()
gamer = Board()

gamer.player_ship_place(ship.little_ship)
gamer.print_board()
