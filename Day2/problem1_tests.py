import unittest

from problem1 import findPoisonedDuration

class TestProblem1(unittest.TestCase):

    def tests(self):
        self.assertEqual(findPoisonedDuration([1,4], 2), 4)
        self.assertEqual(findPoisonedDuration([1,2], 2), 3)
        self.assertEqual(findPoisonedDuration([1,4,5,10], 3), 10)
        self.assertEqual(findPoisonedDuration([1,8,12,13,15,17], 6), 21)

unittest.main()

