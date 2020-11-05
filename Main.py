# импорт классов
from GameLogic import *
from Board import *

gamer_board = Board()
start_player = PlayerShipsPlace()

gamer_board.print_board()
start_player.StartPlayerShips()
