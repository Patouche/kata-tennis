# -*- coding: utf-8 -*-

SCORES = ('0', '15', '30', '40', 'ADV', 'WIN GAME')


class Tennis(object):
    """Tennis game."""

    def __init__(self):
        """Class constructor."""
        self.game = (0, 0)  # Player 1 at index 0, Player 2 at index 1

    def score(self):
        return ':'.join([SCORES[i] for i in self.game])

    def _win_point(self, points):
        self.game = tuple(sum(i) for i in zip(self.game, points))
        if self.game == (4, 4):
            self.game = (3, 3)
        if not self.deuce_activated() and 4 in self.game:
            self._win_point(points=points)

    def player1_win_point(self):
        """Method to invoke when the player 1 win the point."""
        self._win_point(points=(1, 0))

    def player2_win_point(self):
        """Method to invoke when the player 1 win the point."""
        self._win_point(points=(0, 1))

    def deuce_activated(self):
        return self.game in ((3, 3), (3, 4), (4, 3))
