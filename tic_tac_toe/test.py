'Тесты для игры крестики-нолики'

import unittest
import exceptions as excs
from main import TicTacToeGame


class TestValidateNumericInput(unittest.TestCase):
    'Test validate_numeric_input'

    def setUp(self):
        self.game = TicTacToeGame()


class TestProcessInput(unittest.TestCase):
    'Test process_input'

    def setUp(self):
        self.game = TicTacToeGame()

    def test_user_quit(self):
        'Выход по пользовательскому вводу'
        self.assertRaises(
                excs.UserQuitException, self.game.process_input, 'quit',
        )

    def test_out_of_range(self):
        'Невалидное число'
        self.assertRaises(
                excs.InvalidNumberError, self.game.process_input, '10',
        )

    def test_occupied_cell(self):
        'Занята клетка'
        self.game.board[4] = 'X'
        self.assertRaises(
                excs.InvalidNumberError, self.game.process_input, '5',
        )

    def test_unknown_command(self):
        'Неизвестная команда'
        self.assertRaises(
                excs.UnknownCommandError, self.game.process_input, 'asdfa',
        )


class TestCheckGameOver(unittest.TestCase):
    'Test check_game_over'

    def setUp(self):
        self.game = TicTacToeGame()

    def test_draw(self):
        'Ничья'
        self.game.board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
        self.assertRaises(excs.DrawException, self.game.check_game_over)

    def test_winner(self):
        'Есть победитель'
        self.game.board = ['X', 'O', 'O', '.', 'X', '.', '.', '.', 'X']
        self.assertRaises(excs.HaveWinnerException, self.game.check_game_over)


if __name__ == '__main__':
    unittest.main()
