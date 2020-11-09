# импорт классов
from Ship import *


class GameBehavior(Ships):
    count_ships = 0  # Флаг для подсчета установленных кораблей

    def arrange_ships(self, gamer_choice, gamer_board, gamer):
        gamer_board.print_board()
        while self.count_ships < 1:
            self.ship_place_fire_ship(self.little_ship, gamer_choice(gamer_board), gamer_board)
            self.count_ships += 1
            print(f'Корабль №{self.count_ships} легкого класса расположен ')
            if self.count_ships == 1:
                self.count_ships = 0
                while self.count_ships < 1:
                    self.medium_ship_place(self.medium_ship, gamer_choice(gamer_board), gamer_board, gamer)
                    self.count_ships += 1
                    print(f'Корабль №{self.count_ships} среднего класса расположен ')
                    if self.count_ships == 10:
                        self.count_ships = 0
                        while self.count_ships < 1:
                            self.large_ship_place(self.large_ship, gamer_choice(gamer_board), gamer_board, gamer)
                            self.count_ships = 11
                            print(f'Корабль высшего класса расположен ')
                            return

    # Функция для выстрела по доске противника
    def fire(self, gamer_choice, gamer_board, enemy_board):  # на вход принимает функцию ввода координит,
        print('Сделайте выстрел по доске противника!')
        print(enemy_board.print_board())
        self.ship_fire(self.burning_ship, gamer_choice(gamer_board, enemy_board), gamer_board, enemy_board)

