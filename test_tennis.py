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

    def test_2_players_reach_the_score_40_then_the_DEUCE_rule_is_activated(self):
        tennis = Tennis()
        tennis.game = (3, 2)

        tennis.player2_win_point()

        self.assertEqual(tennis.score(), '40:40')
        self.assertTrue(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_score_is_DEUCE_and_when_player_1_win_the_point_then_player_1_take_the_ADVANTAGE(self):
        tennis = Tennis()
        tennis.game = (3, 3)

        tennis.player1_win_point()

        self.assertEqual(tennis.score(), 'ADV:40')
        self.assertTrue(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_the_player_who_has_the_ADVANTAGE_win_the_point_then_he_win_the_game(self):
        tennis = Tennis()
        tennis.game = (4, 3)

        tennis.player1_win_point()

        self.assertEqual(tennis.score(), 'WIN GAME:40')
        self.assertFalse(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_the_player_who_has_the_ADVANTAGE_loose_the_point_then_the_score_is_DEUCE(self):
        tennis = Tennis()
        tennis.game = (4, 3)

        tennis.player2_win_point()

        self.assertEqual(tennis.score(), '40:40')
        self.assertTrue(tennis.deuce_activated(), 'The deuce rule is activated')


if __name__ == '__main__':
    unittest.main()
