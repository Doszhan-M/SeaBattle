# импорт классов
from GameLogic import *
from Board import *

gamer_board = Board()
start_player = ShipsLocation()
computer = ShipsLocation()

computer.arrange_ships(Gamer.computer_choice)
start_player.arrange_ships(Gamer.player_choice)

