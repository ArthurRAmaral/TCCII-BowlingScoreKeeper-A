import unittest
from .frame import Frame


class TestFrames(unittest.TestCase):
    def test_frame(self):
        frame = Frame(2, 4)
        self.assertEqual(frame.first_throw, 2)
        self.assertEqual(frame.second_throw, 4)

    def test_frame_score(self):
        frame = Frame(2, 6)
        score = frame.score()
        self.assertEqual(score, 8)

        frame = Frame(0, 9)
        score = frame.score()
        self.assertEqual(score, 9)

    def test_is_strike(self):
        frame = Frame(10, 0)
        is_strike = frame.is_strike()
        self.assertTrue(is_strike)

        frame = Frame(9, 1)
        is_strike = frame.is_strike()
        self.assertFalse(is_strike)

        frame = Frame(0, 10)
        is_strike = frame.is_strike()
        self.assertFalse(is_strike)

        frame = Frame(3, 2)
        is_strike = frame.is_strike()
        self.assertFalse(is_strike)

        # test bonus frame with 2 strikes
        frame = Frame(10, 10)
        is_strike = frame.is_strike()
        self.assertFalse(is_strike)

    def test_is_spare(self):
        frame = Frame(9, 1)
        is_spare = frame.is_spare()
        self.assertTrue(is_spare)

        frame = Frame(0, 10)
        is_spare = frame.is_spare()
        self.assertTrue(is_spare)

        frame = Frame(10, 0)
        is_spare = frame.is_spare()
        self.assertFalse(is_spare)

        frame = Frame(3, 2)
        is_spare = frame.is_spare()
        self.assertFalse(is_spare)


if __name__ == '__main__':
    unittest.main()
