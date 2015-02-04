import unittest

from simple_db.simple_db import SimpleDB

class TestSimpleDB(unittest.TestCase):
    
    def test_set_get(self):
        test_db = SimpleDB()
        test_db.set('a',10)
        self.assertEqual(test_db.get('a'), 10)
        test_db.set('a',100)
        self.assertEqual(test_db.get('a'), 100)
        
        
    def test_set_num_equal_to(self):
        test_db = SimpleDB()
        test_db.set('a',10)
        test_db.set('b',10)
        test_db.set('c',10)
        self.assertEqual(test_db.num_equal_to(10), 3)
        test_db.set('a',20)
        self.assertEqual(test_db.num_equal_to(10), 2)
        self.assertEqual(test_db.num_equal_to(20), 1)

    
    def test_unset(self):
        test_db = SimpleDB()
        test_db.set('a',10)
        self.assertEqual(test_db.get('a'), 10)
        test_db.unset('a')
        self.assertEqual(test_db.get('a'), None)

