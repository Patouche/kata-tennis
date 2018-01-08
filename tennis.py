# -*- coding: utf-8 -*-

SCORES = ('0', '15', '30', '40', 'WIN GAME')


class Tennis(object):
    """Tennis game."""

    def __init__(self):
        """Class constructor."""
        self.game = (0, 0)

    def score(self):
        return ':'.join(tuple(map(str, self.game)))

    def _win_point(self, param):
        pass

    def player1_win_point(self):
        """Method to invoke when the player 1 win the point."""
        self._win_point((1, 0))

    def player2_win_point(self):
        """Method to invoke when the player 1 win the point."""
        self._win_point((0, 1))
