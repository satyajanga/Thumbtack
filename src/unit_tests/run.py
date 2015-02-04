#!/usr/bin/python
import unittest
import sys
import test_simple_db

def main():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_simple_db))
    return unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    if main().wasSuccessful():
        sys.exit(0)
    sys.exit(1)
