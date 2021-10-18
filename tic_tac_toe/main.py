'Модуль с описанием класса игры в крестики-нолики'

import exceptions as excs


class TicTacToeGame:
    'Экземпляр игры'

    WINNING_LINES = (
            {0, 3, 6},
            {1, 4, 7},
            {2, 5, 8},
            {0, 1, 2},
            {3, 4, 5},
            {6, 7, 8},
            {0, 4, 8},
            {2, 4, 6},
    )

    def __init__(self):
        self.turn = 'X'
        self.board = ['.' for i in range(9)]

    def start_game(self):
        'Запуск игры'

        self.print_intro()
        while True:
            print(f'Ходит {self.turn}')
            try:
                print('> ', end='')
                cmd = input()
                self.process_input(cmd)
            except excs.InputValidationError as exc:
                print(exc)
                TicTacToeGame.print_help()
            except (excs.GameOverException, excs.UserQuitException) as exc:
                print(exc)
                break

    def print_intro(self):
        'Вывод вступительных слов'

        print('Привет! Это крестики-нолики :)\n')
        TicTacToeGame.print_help()
        print('Для хода введите номер клетки:')
        self.print_tip()

    def print_board(self, board=None):
        'Вывод переданной доски. По умолчанию - текущее состояние игры'

        if board is None:
            board = self.board

        print(r' + - - - + ')
        print(f' | {board[0]} {board[1]} {board[2]} | ')
        print(f' | {board[3]} {board[4]} {board[5]} | ')
        print(f' | {board[6]} {board[7]} {board[8]} | ')
        print(r' + - - - + ')
        print()

    def print_tip(self):
        'Вывод подсказки для ввода'

        self.print_board(board=list(range(1, 10)))

    @staticmethod
    def print_help():
        'Вывод доступных команд'

        print('Доступные комманды:')
        print('    > N - сделать ход в клетку с номером N')
        print('    > tip - напомнить номера клеток номера клеток')
        print('    > board - показать текущее состояние доски')
        print('    > quit - закончить игру')
        print('    > help - показать доступные команды')
        print()

    def process_input(self, cmd):
        'Обработка ввода'

        if cmd == 'help':
            TicTacToeGame.print_help()
        elif cmd == 'tip':
            self.print_tip()
        elif cmd == 'board':
            self.print_board()
        elif cmd == 'quit':
            raise excs.UserQuitException('До новых встреч!')
        else:
            num = self.validate_numeric_input(cmd)
            self.make_move(num)

    def validate_numeric_input(self, cmd):
        'Валидация числового ввода'

        try:
            num = int(cmd) - 1
        except ValueError as exc:
            raise excs.UnknownCommandError('Неизвестная команда!') from exc

        if num < 0 or num > 8:
            raise excs.InvalidNumberError('Номер клетки должен быть от 1 до 9')

        if self.board[num] != '.':
            raise excs.InvalidNumberError('Клетка уже занята')

        return num

    def make_move(self, num):
        'Ход'

        self.board[num] = self.turn
        self.check_game_over()
        self.print_board()
        self.turn = 'X' if self.turn == 'O' else 'O'

    def check_game_over(self):
        'Проверка конца игры'

        current_positions = {
                i for i in range(len(self.board)) if self.board[i] == self.turn
        }
        for line in self.WINNING_LINES:
            if current_positions.issuperset(line):
                raise excs.HaveWinnerException(f'{self.turn} победил!')

        if self.board.count('.') == 0:
            raise excs.DrawException('Ничья!')


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
