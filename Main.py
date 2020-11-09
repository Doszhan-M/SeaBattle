# импорт классов
from Board import *
from GameLogic import *

gamer_computer = 'computer'
gamer_player = 'player'

start_player = ShipsLocation()
start_computer = ShipsLocation()

player_choice = Gamer()
computer_choice = Gamer()

player_board = Board()
computer_board = Board()

start_computer.arrange_ships(computer_choice.computer_choice, computer_board, gamer_computer)
start_player.arrange_ships(player_choice.player_choice, player_board, gamer_player)
