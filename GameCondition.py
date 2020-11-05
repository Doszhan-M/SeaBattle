class GameCondition:
    computer_step_list = set()  # Переменная для сбора сделанных ходов компьютера
    player_step_list = set()    # Переменная для сбора сделанных ходов игрока
    block_list = set()          # Переменная для сбора всех сделанных ходов обоих игроков
    one_cell_work_list = set()  # переменная для вычисления минимального расстояния между кораблями
    access_cell_board = set()   # Переменная для хранения вариантов хода крупных кораблей
    allow_list = set()  # Переменная где храняться доступные ходы
    list_all_step = set()  # Переменная где храняться все ходы
    # Вспомогательные переменные конструктора доступных ходов
    list2 = ('a', 'b', 'c', 'd', 'e', 'f')
    list3 = ('1', '2', '3', '4', '5', '6')
    flag = 0

    # Создаем множество всех доступных вариантов
    def __init__(self):
        for i in self.list2:
            for y in self.list3:
                self.list_all_step.add(i + y)
        self.access_cell_board.update(self.list_all_step)
