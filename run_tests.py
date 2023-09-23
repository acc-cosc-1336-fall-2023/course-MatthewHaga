#from tests.examples.c_decisions import tests_decisions
##from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.homework.b_in_proc_out import tests_in_proc_out
##from tests.examples.a_example import tests_devprocess
#from tests.homework.c_decisions import tests_decisions
import unittest
from tests.examples.d_repetition import tests_repetition
#from tests.examples.d_repetition import tests_repetition
from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)