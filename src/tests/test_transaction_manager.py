import unittest

from simple_db.transaction_manager import TransactionManager

class TestTransactionManager(unittest.TestCase): 
    def test_set_get(self):
        tx_manager = TransactionManager()
        tx_manager.handle_set('a',10)
        self.assertEqual(tx_manager.handle_get('a'), 10)
        tx_manager.handle_set('a',100)
        self.assertEqual(tx_manager.handle_get('a'), 100)
        
        
    def test_set_num_equal_to(self):
        tx_manager = TransactionManager()
        tx_manager.handle_set('a',10)
        tx_manager.handle_set('b',10)
        tx_manager.handle_set('c',10)
        self.assertEqual(tx_manager.handle_num_equal_to(10), 3)
        tx_manager.handle_set('a',20)
        self.assertEqual(tx_manager.handle_num_equal_to(10), 2)
        self.assertEqual(tx_manager.handle_num_equal_to(20), 1)

    
    def test_unset(self):
        tx_manager = TransactionManager()
        tx_manager.handle_set('a',10)
        self.assertEqual(tx_manager.handle_get('a'), 10)
        tx_manager.handle_unset('a')
        self.assertEqual(tx_manager.handle_get('a'), None)

    def test_rollback(self):
        tx_manager = TransactionManager()
        tx_manager.handle_set('a',10)
        tx_manager.handle_begin()
        tx_manager.handle_set('a',20)
        self.assertEqual(tx_manager.handle_get('a'), 20)
        tx_manager.handle_rollback()
        self.assertEqual(tx_manager.handle_get('a'), 10)
        tx_manager.handle_begin()
        tx_manager.handle_unset('a')
        self.assertEqual(tx_manager.handle_get('a'), None)

    def test_commit(self):
        tx_manager = TransactionManager()
        tx_manager.handle_set('a',10)
        tx_manager.handle_begin()
        tx_manager.handle_unset('a')
        tx_manager.handle_begin()
        tx_manager.handle_set('b',20)
        tx_manager.handle_commit()
        self.assertEqual(tx_manager.handle_get('b'), 20)
        self.assertEqual(tx_manager.handle_rollback(), "NO TRANSACTION")



        
