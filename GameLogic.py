# импорт классов
from Ship import *


class GameBehavior(Ships):
    count_ships = 0  # Флаг для подсчета установленных кораблей
    game_cycle = 'continue'
    fire_count = 0

    def arrange_ships(self, gamer_choice, gamer_board, gamer):
        time.sleep(0.5)
        gamer_board.print_board()
        time.sleep(0.5)
        #self.large_ship_place(self.large_ship, gamer_choice(gamer_board, gamer), gamer_board, gamer)
        self.count_ships += 1
        time.sleep(0.5)
        print(colored('Корабль высшего класса расположен! ', 'green'))
        if self.count_ships == 1:
            self.count_ships = 0
            while self.count_ships < 2:
                time.sleep(0.5)
                self.medium_ship_place(self.medium_ship, gamer_choice(gamer_board, gamer), gamer_board, gamer)
                self.count_ships += 1
                time.sleep(0.5)
                print(colored(f'Корабль №{self.count_ships} среднего класса расположен ', 'green'))
                if self.count_ships == 2:
                    self.count_ships = 0
                    while self.count_ships < 4:
                        time.sleep(0.5)
                        self.ship_place(self.little_ship, gamer_choice(gamer_board, gamer), gamer_board, gamer)
                        self.count_ships += 1
                        time.sleep(0.5)
                        print(colored(f'Корабль №{self.count_ships} легкого класса расположен ', 'green'))
        return

    # Функция для выстрела по доске противника
    def fire(self, gamer_shoot, gamer_board, enemy_board, battle_print_board,
             gamer, debug):  # на вход принимает функцию ввода координит и доски игроков
        if gamer == 'player':
            print('Сделайте выстрел по доске противника!')
        if gamer == 'computer':
            print('Компьютер открывает огонь по вашим кораблям!')
        if debug == 'debug':
            enemy_board.print_board()
        else:
            battle_print_board.print_board()
        # Пока выстрел поражает цель соперник продалжает стрельбу
        self.retry_fire(gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer, debug)
        if enemy_board.step_list.issubset(gamer_board.shoot_list):
            print('\n', '  Поздравляем! Вы победили!', '\n', '-'*30)
            time.sleep(1.5)
            enemy_board.print_board()
            gamer_board.print_board()
            game_cycle = 'stop'
            return game_cycle
        if gamer_board.step_list.issubset(enemy_board.shoot_list):
            print('\n', '  Компьютер одержал победу! ')
            time.sleep(1.5)
            gamer_board.print_board()
            enemy_board.print_board()
            game_cycle = 'stop'
            return game_cycle
        else:
            game_cycle = 'continue'
            return game_cycle

    # Функция повтора выстрела если попал
    def retry_fire(self, gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer, debug):
        shoot_result = self.ship_fire(gamer_shoot(gamer_board, enemy_board), gamer_board, enemy_board,
                                      battle_print_board, gamer, debug)
        if shoot_result == self.burning_ship:
            self.fire_count += 1
            if self.fire_count == len(enemy_board.step_list):
                return
            else:
                return self.retry_fire(gamer_shoot, gamer_board, enemy_board, battle_print_board, gamer, debug)
