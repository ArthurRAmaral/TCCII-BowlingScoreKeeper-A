import unittest
from .game import BowlingGame
from .frame import Frame


class TestGames(unittest.TestCase):
    def test_game(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertEqual(len(game.frames), 10)

    def test_game_score(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        score = game.score()
        self.assertEqual(score, 81)

    def test_game_score_with_strike(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        score = game.score()
        self.assertEqual(score, 94)

    def test_game_score_with_spare(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 9))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        score = game.score()
        self.assertEqual(score, 88)

    def test_game_score_with_spare_after_strike(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(4, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        score = game.score()
        self.assertEqual(score, 103)

    def test_game_score_with_multiples_strikes(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        score = game.score()
        self.assertEqual(score, 112)

    def test_game_score_with_multiples_spares(self):
        game = BowlingGame()

        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(5, 5))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        score = game.score()
        self.assertEqual(score, 98)

    def test_game_score_with_spare_at_last_frame(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 8))

        game.add_frame(Frame(7, 0))

        score = game.score()
        self.assertEqual(score, 90)

    def test_game_score_with_strike_at_last_frame(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(10, 0))

        game.add_frame(Frame(7, 2))

        score = game.score()
        self.assertEqual(score, 92)

    def test_game_score_with_spare_at_last_frame_and_strike_at_bonus(self):
        game = BowlingGame()

        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 8))

        game.add_frame(Frame(10, 0))

        score = game.score()
        self.assertEqual(score, 93)

    def test_best_game_score_possible(self):
        game = BowlingGame()

        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))

        game.add_frame(Frame(10, 10))

        score = game.score()
        self.assertEqual(score, 300)

    def test_real_game(self):
        game = BowlingGame()

        game.add_frame(Frame(6, 3))
        game.add_frame(Frame(7, 1))
        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(6, 2))
        game.add_frame(Frame(7, 3))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(8, 0))
        game.add_frame(Frame(7, 3))

        game.add_frame(Frame(10, 0))

        score = game.score()
        self.assertEqual(score, 135)


if __name__ == '__main__':
    unittest.main()
