# импорт классов
from Ship import *


class GameBehavior(Ships):
    count_ships = 0  # Флаг для подсчета установленных кораблей
    game_cycle = 'continue'
    fire_count = 0

    def arrange_ships(self, gamer_choice, gamer_board, gamer):
        gamer_board.print_board()
        while self.count_ships < 1:
            self.ship_place(self.little_ship, gamer_choice(gamer_board), gamer_board, gamer)
            self.count_ships += 1
            print(f'Корабль №{self.count_ships} легкого класса расположен ')
            if self.count_ships == 1:
                self.count_ships = 0
                while self.count_ships < 1:
                    self.medium_ship_place(self.medium_ship, gamer_choice(gamer_board), gamer_board, gamer)
                    self.count_ships += 1
                    print(f'Корабль №{self.count_ships} среднего класса расположен ', '\n')
                    if self.count_ships == 10:
                        self.count_ships = 0
                        while self.count_ships < 1:
                            self.large_ship_place(self.large_ship, gamer_choice(gamer_board), gamer_board, gamer)
                            self.count_ships = 11
                            print(f'Корабль высшего класса расположен ', '\n', 'Все корабли заняли свои позиции.' )
                            return

    # Функция для выстрела по доске противника
    def fire(self, gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer):  # на вход принимает функцию ввода координит и доски игроков
        print('Сделайте выстрел по доске противника!')
        battle_print_board.print_board()
        # Пока выстрел поражает цель соперник продалжает стрельбу
        self.retry_fire(gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer)
        if enemy_board.step_list.issubset(gamer_board.shoot_list):
            print('Вы победили! ')
            game_cycle = 'stop'
            return game_cycle
        if gamer_board.step_list.issubset(enemy_board.shoot_list):
            print('Компьютер одержал победу! ')
            game_cycle = 'stop'
            return game_cycle
        else:
            game_cycle = 'continue'
            return game_cycle

    # Функция повтора выстрела если попал
    def retry_fire(self, gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer):
        shoot_result = self.ship_fire(gamer_shoot(gamer_board, enemy_board), gamer_board, enemy_board, battle_print_board, gamer)
        if shoot_result == self.burning_ship:
            self.fire_count += 1
            if self.fire_count == len(enemy_board.step_list):
                return
            else:
                return self.retry_fire(gamer_shoot, gamer_board, enemy_board, battle_print_board)
