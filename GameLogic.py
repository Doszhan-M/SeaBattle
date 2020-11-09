# импорт классов
from Ship import *


class ShipsLocation(PlayerShips):
    count_ships = 0  # Флаг для подсчета установленных кораблей

    def arrange_ships(self, gamer_choice, gamer_board, port):
        gamer_board.print_board()
        while self.count_ships < 1:
            self.player_little_ship_place(self.little_ship, gamer_choice(), gamer_board)
            self.count_ships += 1
            print(f'Корабль №{self.count_ships} легкого класса расположен ')
            if self.count_ships == 1:
                self.count_ships = 0
                while self.count_ships < 1:
                    self.player_medium_ship_place(self.medium_ship, gamer_choice(), gamer_board, port)
                    self.count_ships += 1
                    print(f'Корабль №{self.count_ships} среднего класса расположен ')
                    if self.count_ships == 10:
                        self.count_ships = 0
                        while self.count_ships < 1:
                            self.player_large_ship_place(self.large_ship, gamer_choice(), gamer_board, port)
                            self.count_ships = 11
                            print(f'Корабль высшего класса расположен ')
                            return
