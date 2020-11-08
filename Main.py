# импорт классов
from GameLogic import *
from Board import *

gamer_computer = 'computer'
gamer_player = 'player'
start_player1 = GameCondition()
start_player = ShipsLocation()

start_computer = ShipsLocation()
start_computer1 = GameCondition()

gamer_choice = Gamer()
computer_choice = Gamer()

player_board = Board()
computer_board = Board()



start_computer.arrange_ships(computer_choice.computer_choice, gamer_computer)
start_player.arrange_ships(gamer_choice.player_choice, gamer_player)


