'Описание всех исключений игры'


class GameOverException(Exception):
    'Конец игры по причине ничьи или победы одного из игроков'


class HaveWinnerException(GameOverException):
    'Конец игры по причины победы одного из игроков'


class DrawException(GameOverException):
    'Конец игры по причине ничьи'


class UserQuitException(Exception):
    'Принудительное завершение игры от пользователя'


class InputValidationError(Exception):
    'Ошибка валидации пользовательского ввода'


class InvalidNumberError(InputValidationError):
    'Введено неверное число'


class UnknownCommandError(InputValidationError):
    'Введена неизвестная команда'
