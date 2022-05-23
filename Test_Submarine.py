import unittest
from Submarines import Submarines


class TestSubmarinesCounter(unittest.TestCase):
    def test1_native_way(self):
        s = Submarines([[1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0]])
        self.assertEqual(s.count_submarines_naive_way(), 4)

    def test2_native_way(self):
        s = Submarines([[1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 1, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0]])
        self.assertEqual(s.count_submarines_naive_way(), 6)

    def test3_native_way(self):
        s = Submarines([[0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 1, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 1, 0, 1, 0, 0]])
        self.assertEqual(s.count_submarines_naive_way(), 9)

    def test4_native_way(self):
        s = Submarines([[0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1]])
        self.assertEqual(s.count_submarines_naive_way(), 2)


if __name__ == '__main__':
    unittest.main()
