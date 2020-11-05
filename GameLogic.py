# импорт классов
from Ship import *


class PlayerShipsPlace(PlayerShips):
    count = 0

    def StartPlayerShips(self):
        while self.count < 3:
            self.player_little_ship_place(self.little_ship, self.player_choice())
            self.count += 1
            print(f'Корабль №{self.count} легкого класса расположен ')
            print('Block list', self.block_list)
            if self.count == 1:
                self.count = 0
                while self.count < 3:
                    self.player_medium_ship_place(self.medium_ship, self.player_choice())
                    self.count += 1
                    print(f'Корабль №{self.count} среднего класса расположен ')
                    print('Block list', self.block_list)
                    if self.count == 1:
                        self.count = 0
                        while self.count < 1:
                            self.player_large_ship_place(self.large_ship, self.player_choice())
                            self.count = 5
                            print(f'Корабль №{self.count} высшего класса расположен ')
                            print('Block list', self.block_list)
