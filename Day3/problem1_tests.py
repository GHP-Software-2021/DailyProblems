import unittest

from problem1 import numJewelsInStones

class TestProblem1(unittest.TestCase):

    def tests(self):
        self.assertEqual(numJewelsInStones("a", "aaaa"), 4)
        self.assertEqual(numJewelsInStones("a0b", "bbce3"), 2)
        self.assertEqual(numJewelsInStones("aAz", "zzzmneAefeijefz321A"), 6)
        self.assertEqual(numJewelsInStones("rgb", "25502553gr44asdb"), 3)

unittest.main()

