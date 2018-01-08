# -*- coding: utf-8 -*-

SCORES = ('0', '15', '30', '40', 'ADV', 'WIN GAME')


class Tennis(object):
    """Tennis game."""

    def __init__(self):
        """Class constructor."""
        self.game = (0, 0)  # Player 1 at index 0, Player 2 at index 1
        self.set = (0, 0)  # Player 1 at index 0, Player 2 at index 1
        self.match = []  # Match set history

    def _win_point(self, points):
        if 5 in self.game:
            self.game = (0, 0)
        self.game = tuple(sum(i) for i in zip(self.game, points))
        if self.game == (4, 4):
            self.game = (3, 3)
        if not self.deuce_activated() and 4 in self.game:
            self._win_point(points=points)
            self._win_game(game=points)

    def _win_game(self, game):
        self.set = tuple(sum(x) for x in zip(self.set, game))
        diff = max(self.set) - min(self.set)
        if 7 in self.set or (6 in self.set and diff >= 2):
            self._win_set()

    def _win_set(self):
        self.match.append(self.score_set())
        self.set = (0, 0)

    def player1_win_point(self):
        """Method to invoke when the player 1 win the point."""
        self._win_point(points=(1, 0))

    def player2_win_point(self):
        """Method to invoke when the player 1 win the point."""
        self._win_point(points=(0, 1))

    def deuce_activated(self):
        """Return true if the game is deuce. False otherwise."""
        return self.game in ((3, 3), (3, 4), (4, 3))

    def score_game(self):
        """ Get the score of the current game using format : '15:30'."""
        return ':'.join([SCORES[i] for i in self.game])

    def score_set(self):
        """Get the score of the current set using format : '6:4'."""
        return ':'.join(tuple(map(str, self.set)))

    def score_match(self):
        """Get the score of the match using format : '6:4, 6:4, 00'."""
        return ', '.join(self.match + [self.score_set()])
