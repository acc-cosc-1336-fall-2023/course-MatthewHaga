import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
     def test_get_options_ratio(self):
        self.assertEqual(.85, get_options_ratio(85,100))
        self.assertEqual(0, get_options_ratio(0,100))
        self.assertEqual(1, get_options_ratio(100,100))

def test_get_faculty_rating(self):
        self.assertEqual('is Excellent!', get_faculty_rating(.91))
        self.assertEqual('is Very Good', get_faculty_rating(.85))
        self.assertEqual('is Good', get_faculty_rating(.71))
        self.assertEqual('Needs Improvement', get_faculty_rating(.66))
        self.assertEqual('is Unacceptable...', get_faculty_rating(.45))
        self.assertEqual('is impossible.', get_faculty_rating(1.01))