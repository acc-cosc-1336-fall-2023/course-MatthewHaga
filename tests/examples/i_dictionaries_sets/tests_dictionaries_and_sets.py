import unittest

from src.examples.i_dictionaries_sets.dictionaries import difference_and_add, play_both_sports, play_sports_union, plays_1st_sport, plays_2nd_sport, plays_one_sport, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
        

    def test_play_both_sports(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(play_both_sports(basketball,baseball) , set(['Carmen', 'Alicia']))

    def test_plays_one_sport(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(plays_one_sport(basketball,baseball) , set(['Jodi', 'Aida','Eva', 'Sarah']))

    def test_play_sports_union(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(play_sports_union(baseball,basketball), set(['Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah']))

    def test_play_1st_sports_only(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(plays_1st_sport(baseball,basketball), set(['Jodi', 'Aida']))

    def test_play_2nd_sports_only(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(plays_2nd_sport(baseball,basketball), set(['Eva', 'Sarah']))

    def test_difference_and_add(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
        self.assertEqual(difference_and_add(baseball,basketball), (set(['Jodi', 'Aida']),set(['Eva', 'Sarah'])))

