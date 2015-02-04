#!/usr/bin/python
import unittest
import sys
import os
def main():
    sys.path.append(os.path.abspath('../'))
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    import test_simple_db, test_integration, test_transaction_manager
    suite.addTests(loader.loadTestsFromModule(test_simple_db))
    suite.addTests(loader.loadTestsFromModule(test_transaction_manager))
    suite.addTests(loader.loadTestsFromModule(test_integration))
    return unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    if main().wasSuccessful():
        sys.exit(0)
    sys.exit(1)
