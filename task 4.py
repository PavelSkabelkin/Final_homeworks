class Cell:
    def __init__(self, number):
        self.number = number  # Номер клетки
        self.value = ' '  # Изначально клетка пуста

    def __str__(self):
        return self.value

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]  # Создаем список из 9 клеток

    def display(self):
        for i in range(0, 9, 3):
            row = [str(cell) for cell in self.cells[i:i+3]]
            print('|'.join(row))
            if i < 6:
                print('-' * 5)

    def is_full(self):
        return all(cell.value != ' ' for cell in self.cells)

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные линии
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные линии
            (0, 4, 8), (2, 4, 6)              # Диагонали
        ]

        for combo in winning_combinations:
            values = [self.cells[i].value for i in combo]
            if all(v == values[0] and v != ' ' for v in values):
                return True  # Найден победитель

        return False  # Нет победителя

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board, cell_number):
        cell = board.cells[cell_number - 1]
        if cell.value == ' ':
            cell.value = self.symbol
            return True
        else:
            print("Эта клетка уже занята. Пожалуйста, выберите другую.")
            return False

board = Board()
player1 = Player("Игрок 1", "X")
player2 = Player("Игрок 2", "O")

current_player = player1

while not board.is_full():
    board.display()
    try:
        cell_number = int(input(f"{current_player.name}, выберите номер клетки (1-9): "))
        if 1 <= cell_number <= 9:
            if current_player.make_move(board, cell_number):
                board.display()
                if board.check_winner():
                    print(f"{current_player.name} победил!")
                    break
                elif board.is_full():
                    print("Ничья! На доске нет свободных клеток.")
                    break
                else:
                    current_player = player2 if current_player == player1 else player1
            else:
                print("Эта клетка уже занята. Пожалуйста, выберите другую.")
        else:
            print("Недопустимое значение. Введите число от 1 до 9.")
    except ValueError:
        print("Недопустимый ввод. Введите число от 1 до 9.")
