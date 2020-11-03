class Board:
    w = '     1   2   3   4   5   6'
    a = [' a ', '|1|', '|2|', '|3|', '|O|', '|O|', '|6|']
    b = ' b |O| |O| |O| |O| |O| |O|'
    c = ' c |O| |O| |O| |O| |O| |O|'
    d = ' d |O| |O| |O| |O| |O| |O|'
    e = ' e |O| |O| |O| |O| |O| |O|'
    f = ' f |O| |O| |O| |O| |O| |O|'

    list1 = [a, b, c, d, e, f]
    number = 0

    def print_board(self):
        print(self.w, '\n', self.a, '\n', self.b, '\n', self.c, '\n', self.d, '\n', self.e, '\n', self.f)

    def player_choice(self):
        input1 = 'a3'
        # input_pattern = 'self.$[@]'
        # input_pattern = input_pattern.replace('$', input1[0])
        # input_pattern = input_pattern.replace('@', input1[1])
        input_pattern = 'self.@'
        input_pattern = input_pattern.replace('@', input1[0])
        self.number = int(input1[1])
        return input_pattern

    def player_ship_place(self):
        self.player_choice()
        index = self.list1.index(eval(self.player_choice()))
        print(index)
        print(self.list1[0][self.number])
        self.list1[0][self.number] = '!'
        print(self.a)


class Ship:
    little_ship = '|#|'


ship = Ship()
gamer = Board()

gamer.player_ship_place()
