# импорт классов
from GameLogic import *

print('\n', colored('Добро пожаловать в игру Морской Бой!', 'magenta'), '\n', '-' * 35, '\n',
      'Сделайте расстановку кораблей на игровой доске.', '\n', 'Сначало установите корабль высшего класса: ')
time.sleep(2)
game = 'start'
while game == 'start':
    # Объявляем переменные для определения когда остановить игру и знать чей ход
    player_cycle = 'continue'
    computer_cycle = 'continue'
    gamer_player = 'player'
    gamer_computer = 'computer'

    # Объявляем классы
    player = GameBehavior(gamer_player)
    computer = GameBehavior(gamer_computer)
    player_choice = Gamer(gamer_player)
    computer_choice = Gamer(gamer_computer)
    player_board = Board(gamer_player)
    player_print_board = Board(gamer_player)
    computer_board = Board(gamer_computer)
    computer_print_board = Board(gamer_computer)

    # Начинаем игру с расстановки кораблей
    player.arrange_ships(player_choice.player_choice, player_board, gamer_player)
    time.sleep(1)
    print('Ход переходит к сопернику, компьютер расставляет свои корабли...')
    time.sleep(0.2)
    print('.' * 5)
    time.sleep(1)
    computer.arrange_ships(computer_choice.computer_choice, computer_board, gamer_computer)
    time.sleep(1)
    print(colored('Все корабли заняли свои позиции.', 'red'), '\n')
    debug = input('Если хотите видеть доску компьютера в открытом виде, то наберите debug. '
                  'Если хотите играть честно, нажмите любую клавищу: ')
    print(colored('Бой начинается!', 'red'), '\n', '-' * 12)
    time.sleep(1)

    # Соперники начинают огонь друг по другу
    while player_cycle and computer_cycle == 'continue':
        player_cycle = player.fire(player_choice.player_shoot, player_board, computer_board, computer_print_board,
                                   gamer_player, debug)
        if player_cycle == 'stop':
            break
        computer_cycle = computer.fire(computer_choice.computer_shoot, computer_board, player_board, player_print_board,
                                       gamer_computer, debug)

    game = input(
        'Если хотите начать игру заново наберите start, если жалаете остановить игру нажмите любую клавишу: ')
