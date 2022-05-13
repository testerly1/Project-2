import RockPaperScissorsEsterly
import unittest


class TestRPS(unittest.TestCase):
    def test_game(self):
        self.assertEquals(RockPaperScissorsEsterly.game, 1)
        with self.assertRaises(TypeError):
            RockPaperScissorsEsterly.game()

    def test_reset(self):
        self.assertEquals(RockPaperScissorsEsterly.reset, 0)
        with self.assertRaises(TypeError):
            RockPaperScissorsEsterly.reset()


if __name__ == '__main__':
    unittest.main()
