# импорт классов
from Ship import *


class ShipsLocation(PlayerShips):

    def arrange_ships(self, choice):
        self.print_board()
        while self.count < 1:
            self.player_little_ship_place(self.little_ship, choice(self))
            self.count += 1
            print(f'Корабль №{self.count} легкого класса расположен ')
            if self.count == 1:
                self.count = 0
                while self.count < 3:
                    self.player_medium_ship_place(self.medium_ship, choice(self))
                    self.count += 1
                    print(f'Корабль №{self.count} среднего класса расположен ')
                    if self.count == 1:
                        self.count = 0
                        while self.count < 1:
                            self.player_large_ship_place(self.large_ship, choice(self))
                            self.count = 11
                            print(f'Корабль высшего класса расположен ')
