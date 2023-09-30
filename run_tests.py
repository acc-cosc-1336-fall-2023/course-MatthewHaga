import unittest

from tests.homework.d_repetition import tests_repetition
from tests.homework.e_functions import tests_functions

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suite) 