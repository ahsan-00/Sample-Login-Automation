# run_tests.py
import unittest
import sys
sys.path.insert(0, './')

from tests.test_signup import TestSignup

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSignup)
    unittest.TextTestRunner(verbosity=2).run(suite)