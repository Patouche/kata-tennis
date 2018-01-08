# -*- coding: utf-8 -*-
import unittest

from tennis import Tennis


class TestTennis(unittest.TestCase):
    def test_game_starts_with_a_score_of_0_point_for_each_player(self):
        tennis = Tennis()

        score = tennis.score()

        self.assertEqual(score, '0:0')

    def test_players_score_progress(self):
        tennis = Tennis()
        tennis.player1_win_point()
        tennis.player2_win_point()

        self.assertEqual(tennis.score(), '15:15')
        self.assertIsInstance(tennis.game, tuple)
        self.assertEqual(tennis.game, (1, 1))

        tennis.player1_win_point()
        tennis.player2_win_point()

        self.assertEqual(tennis.score(), '30:30')

        tennis.player1_win_point()

        self.assertEqual(tennis.score(), '40:30')

        tennis.player1_win_point()

        self.assertEqual(tennis.score(), 'WIN GAME:30')


if __name__ == '__main__':
    unittest.main()
