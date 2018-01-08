# -*- coding: utf-8 -*-
import unittest

from tennis import Tennis


class TestTennis(unittest.TestCase):
    def test_game_starts_with_a_score_of_0_point_for_each_player(self):
        game = Tennis()

        score = game.score()

        self.assertEqual(score, '0:0')


if __name__ == '__main__':
    unittest.main()
