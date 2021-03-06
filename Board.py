from termcolor import colored
import colorama
colorama.init()


class Board:
    # Игровая доска
    def __init__(self, gamer):
        if gamer == 'player':
            self.z = [colored('        Ваша игровая доска ', 'blue')]
        elif gamer == 'computer':
            self.z = [colored('     Игровая доска компьютера ', 'blue')]
        self.w = ['    ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ']
        self.a = [' a ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
        self.b = [' b ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
        self.c = [' c ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
        self.d = [' d ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
        self.e = [' e ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
        self.f = [' f ', '|0|', '|0|', '|0|', '|O|', '|O|', '|0|']
        self.board_list = [self.a, self.b, self.c, self.d, self.e, self.f]
        # Вспомогательные переменные для функции интерактива с игроком
        self.list_all_step = set()       # Переменная где хранятся все ходы
        self.step_list = set()           # Переменная для сбора сделанных ходов игрока
        self.one_cell_work_list = set()  # Переменная для вычисления минимального расстояния между кораблями
        self.access_cell_board = set()   # Переменная для хранения вариантов хода крупных кораблей
        self.allow_list = set()          # Переменная где хранятся доступные ходы
        self.flag = 0                    # Флаг для ограничения расстояния кораблей
        self.shoot_list = set()          # Переменные для выстрела
        # Переменные для конструктора
        self.list2 = ('a', 'b', 'c', 'd', 'e', 'f')
        self.list3 = ('1', '2', '3', '4', '5', '6')

        # Создаем множество всех доступных вариантов
        for i in self.list2:
            for y in self.list3:
                self.list_all_step.add(i + y)

    # Функция печати доски
    def print_board(self):
        print(*self.z, '\n', *self.w, '\n', *self.a, '\n', *self.b, '\n', *self.c, '\n', *self.d, '\n', *self.e, '\n',
              *self.f, '\n',
              '_' * 30)

    # Функция для определения минимальной дистанции между кораблями на игровой доске
    def min_distance(self):
        for i in self.step_list:  #
            self.one_cell_work_list.add(i.replace(i[1], str(int(i[1]) + 1)))
            self.one_cell_work_list.add(i.replace(i[1], str(int(i[1]) - 1)))
            for y in self.list2:
                if i[0] in y:
                    # При построении листа дистанции может возникнуть исключение, если выбрать клетку близко к краям
                    try:
                        self.one_cell_work_list.add(i.replace(i[0], self.list2[self.list2.index(y) + 1]))
                        self.one_cell_work_list.add(i.replace(i[0], self.list2[abs(self.list2.index(y) - 1)]))
                    # После отлова исключение можно изменить код на более безопасный
                    except IndexError:
                        self.one_cell_work_list.add(i.replace(i[0], self.list2[abs(self.list2.index(y) - 1)]))
        return self.one_cell_work_list
