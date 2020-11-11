# импорт классов
from GameLogic import *
game_cycle = 1
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
while game_cycle == 1:
    game_cycle = player.fire(player_choice.player_shoot, player_board, computer_board)
    print('game_cycle2', game_cycle)
    game_cycle = computer.fire(computer_choice.computer_shoot, computer_board, player_board)
    print('game_cycle3', game_cycle)


