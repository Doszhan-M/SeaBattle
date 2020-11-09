# импорт классов
from GameLogic import *

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
# Соперники окрывают огонь друг другу
while True:
    player.fire(player_choice.player_shoot, player_board, computer_board)
