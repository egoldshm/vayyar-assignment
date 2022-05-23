import unittest
from Submarines import Submarines

s1 = Submarines([[1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0]])

s2 = Submarines([[1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0]])

s3 = Submarines([[0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0],
                [1, 1, 1, 0, 1, 0, 0]])

s4 = Submarines([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1]])


class TestSubmarinesCounter(unittest.TestCase):

    def test1_native_way(self):
        self.assertEqual(s1.count_submarines_naive_way(), 4)

    def test2_native_way(self):
        self.assertEqual(s2.count_submarines_naive_way(), 6)

    def test3_native_way(self):
        self.assertEqual(s3.count_submarines_naive_way(), 9)

    def test4_native_way(self):
        self.assertEqual(s4.count_submarines_naive_way(), 2)

    def test1_better_way(self):
        self.assertEqual(s1.count_submarines_better_way(), 4)

    def test2_better_way(self):
        self.assertEqual(s2.count_submarines_better_way(), 6)

    def test3_better_way(self):
        self.assertEqual(s3.count_submarines_better_way(), 9)

    def test4_better_way(self):
        self.assertEqual(s4.count_submarines_better_way(), 2)


if __name__ == '__main__':
    unittest.main()
