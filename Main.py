# импорт классов
from GameLogic import *
from Board import *

gamer_board = Board()
computer_board = Board()
start_player = ShipsLocation()
start_computer = ShipsLocation()
gamer_choice = Gamer()
computer_choice = Gamer()

# start_computer.arrange_ships(computer_choice.computer_choice)
start_player.arrange_ships(gamer_choice.player_choice)
# start_computer.arrange_ships(Gamer.computer_choice)

