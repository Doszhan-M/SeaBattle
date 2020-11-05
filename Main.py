# импорт библтеотек
# импорт классов
from Board import *
from Ship import *

ship = Ship()
gamer_board = Board()
player = Player()

count = 0
print(GameLogic.allow_list)
gamer_board.print_board()

while count < 2:
    gamer_board.player_little_ship_place(ship.ship, player.player_choice(player.list_all_step))
    count += 1
    print(f'Корабль №{count} легкого класса расположен ')
    print('Block list', gamer_board.block_list)
    if count == 1:
        count = 0
        while count < 2:
            gamer_board.player_medium_ship_place(ship.ship, player.player_choice(gamer_board.list_all_step))
            count += 1
            print(f'Корабль №{count} среднего класса расположен ')
            print('Block list', gamer_board.block_list)
            if count == 1:
                count = 0
                while count < 1:
                    gamer_board.player_large_ship_place(ship.ship, player.player_choice(gamer_board.list_all_step))
                    count = 5
                    print(f'Корабль №{count} высшего класса расположен ')
                    print('Block list', gamer_board.block_list)
