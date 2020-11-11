# импорт классов
from GameLogic import *

player_cycle = 1
computer_cycle = 1
# Объявляем переменные для определение чей ход
gamer_computer = 'computer'
gamer_player = 'player'
# Объявляем классы
player = GameBehavior()
computer = GameBehavior()

player_choice = Gamer()
computer_choice = Gamer()

player_board = Board()
computer_board = Board()

# Начинаем игру
player.arrange_ships(player_choice.player_choice, player_board, gamer_player)
computer.arrange_ships(computer_choice.computer_choice, computer_board, gamer_computer)

# Соперники начинают огонь друг по другу
while player_cycle and computer_cycle == 1:
    player_cycle = player.fire(player_choice.player_shoot, player_board, computer_board)
    if player_cycle == 0:
        break
    computer_cycle = computer.fire(computer_choice.computer_shoot, computer_board, player_board)
    if computer_cycle == 0:
        break

