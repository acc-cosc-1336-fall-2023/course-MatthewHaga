import unittest

from src.homework.h_strings.strings import get_hamming_distance 

from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)

    def test_get_dna_complement(self):
        self.assertEqual('ACCGGGTTTT', get_dna_complement('AAAACCCGGT'))