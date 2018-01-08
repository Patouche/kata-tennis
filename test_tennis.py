# -*- coding: utf-8 -*-
import unittest

from tennis import Tennis


class TestTennis(unittest.TestCase):
    def test_game_starts_with_a_score_of_0_point_for_each_player(self):
        tennis = Tennis()

        score = tennis.score_game()

        self.assertEqual(score, '0:0')

    def test_players_score_progress(self):
        tennis = Tennis()
        tennis.player1_win_point()
        tennis.player2_win_point()

        self.assertEqual(tennis.score_game(), '15:15')
        self.assertIsInstance(tennis.game, tuple)
        self.assertEqual(tennis.game, (1, 1))

        tennis.player1_win_point()
        tennis.player2_win_point()

        self.assertEqual(tennis.score_game(), '30:30')

        tennis.player1_win_point()

        self.assertEqual(tennis.score_game(), '40:30')

        tennis.player1_win_point()

        self.assertEqual(tennis.score_game(), 'WIN GAME:30')

    def test_2_players_reach_the_score_40_then_the_DEUCE_rule_is_activated(self):
        tennis = Tennis()
        tennis.game = (3, 2)

        tennis.player2_win_point()

        self.assertEqual(tennis.score_game(), '40:40')
        self.assertTrue(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_score_is_DEUCE_and_when_player_1_win_the_point_then_player_1_take_the_ADVANTAGE(self):
        tennis = Tennis()
        tennis.game = (3, 3)

        tennis.player1_win_point()

        self.assertEqual(tennis.score_game(), 'ADV:40')
        self.assertTrue(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_the_player_who_has_the_ADVANTAGE_win_the_point_then_he_win_the_game(self):
        tennis = Tennis()
        tennis.game = (4, 3)

        tennis.player1_win_point()

        self.assertEqual(tennis.score_game(), 'WIN GAME:40')
        self.assertFalse(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_the_player_who_has_the_ADVANTAGE_loose_the_point_then_the_score_is_DEUCE(self):
        tennis = Tennis()
        tennis.game = (4, 3)

        tennis.player2_win_point()

        self.assertEqual(tennis.score_game(), '40:40')
        self.assertTrue(tennis.deuce_activated(), 'The deuce rule is activated')

    def test_when_the_set_starts_then_the_set_score_is_0_game_for_each_player(self):
        tennis = Tennis()

        score = tennis.score_set()
        self.assertEqual(score, '0:0')

    def test_set_evolution(self):
        tennis = Tennis()

        for i in range(1, 5):
            tennis.player1_win_point()  # 15
            tennis.player1_win_point()  # 30
            tennis.player1_win_point()  # 40
            tennis.player1_win_point()  # WIN

            self.assertEqual(tennis.score_match(), '%d:0' % i)
            self.assertEqual(tennis.score_set(), '%d:0' % i)

    def test_when_p1_and_p2_have_5_and_p1_win_the_set_then_a_other_game_in_the_set_should_be_played(self):
        tennis = Tennis()
        tennis.set = (5, 5)
        tennis.game = (3, 0)

        tennis.player1_win_point()

        self.assertEqual(tennis.score_match(), '6:5')
        self.assertEqual(tennis.score_set(), '6:5')

    def test_when_score_is_6_6_and_when_p2_win_2_set_then_p2_win_the_set(self):
        tennis = Tennis()
        tennis.set = (6, 6)
        tennis.game = (0, 3)

        tennis.player2_win_point()

        self.assertEqual(tennis.score_set(), '0:0')
        self.assertEqual(tennis.score_match(), '6:7, 0:0')

if __name__ == '__main__':
    unittest.main()
