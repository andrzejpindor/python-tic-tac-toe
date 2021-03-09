import numpy
from collections import Counter


def _validate_coordinates(move):
    if len(move) != 2 or not move[0].isalnum() and not move[1].isalnum():
        print('You should enter numbers!')
        return False
    else:
        return True


def _print_border():
    print('---------')


def _print_line(line):
    print('| {} {} {} |'.format(line[0], line[1], line[2]))


class Game:
    def __init__(self):
        self._board = numpy.array([' ' for _ in range(9)]).reshape(3, 3)
        self._currentPlayer = 'X'

    def make_move(self, move):
        if not _validate_coordinates(move):
            return False

        col = int(move[0]) - 1
        row = int(move[1]) - 1

        if not self._validate_move(col, row):
            return False

        self._board[col, row] = self._currentPlayer
        self._switch_player()

        return True

    def print_board(self):
        _print_border()
        for line in self._board:
            _print_line(line)
        _print_border()

    def check_finished(self):
        winners = self._get_winners()
        if numpy.any(self._board[:,] == ' '):
            if len(winners) == 1:
                print('{} wins'.format(winners[0]))
                return True
            else:
                return False
        else:
            if len(winners) == 1:
                print('{} wins'.format(winners[0]))
                return True
            else:
                print('Draw')
                return True

    def _validate_move(self, col, row):
        if col < 0 or col > 2 or row < 0 or row > 2:
            print('Coordinates should be from 1 to 3!')
            return False

        if self._board[col, row] != ' ':
            print('The cell is occupied! Choose another one!')
            return False

        return True

    def _switch_player(self):
        self._currentPlayer = 'O' if self._currentPlayer == 'X' else 'X'

    def _get_winners(self):
        winners = []
        for x in self._board:
            if len(Counter(x)) == 1 and x[0] != ' ':
                winners.append(x[0])

        for i in range(3):
            if self._board[0, i] == self._board[1, i] == self._board[2, i] and self._board[1, i] != ' ':
                winners.append(self._board[0, i])

        if self._board[0, 0] == self._board[1, 1] == self._board[2, 2] and self._board[0, 0] != ' ':
            winners.append(self._board[0, 0])

        if self._board[0, 2] == self._board[1, 1] == self._board[2, 0] and self._board[0, 2] != ' ':
            winners.append(self._board[0, 2])

        return winners

