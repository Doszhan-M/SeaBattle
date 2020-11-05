class GameLogic:
    computer_step_list = set()  # Переменная для сбора сделанных ходов компьютера
    player_step_list = set()  # Переменная для сбора сделанных ходов игрока
    block_list = set()  # Переменная для сбора всех сделанных ходов
    allow_list = set()  # Переменная где храняться доступные ходы

    # Вспомогательные переменные конструктора доступных ходов
    list2 = ('a', 'b', 'c', 'd', 'e', 'f')
    list3 = ('1', '2', '3', '4', '5', '6')
    list_all_step = set()  # Переменная где храняться возможные ходы

    # Создаем множество всех доступных вариантов
    def __init__(self):
        for i in self.list2:
            for y in self.list3:
                self.list_all_step.add(i + y)

    # В список сделанных ходов вносим ходы игрока и компьютера
    block_list.union(computer_step_list, player_step_list)
    # Из списка всех ходов убираем сделанные ходы и вносим их в доступные ходы
    allow_list.union(list_all_step.symmetric_difference(block_list))
