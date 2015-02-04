import unittest
from subprocess import check_output
from config import config

class TestSimpleDB(unittest.TestCase):
    cmd = "python " + config['main_file'] + " < " + config['test_cases_path'] 
    
    def test_set_get_unset(self):
        output = check_output(self.cmd + "/input1.txt", shell = True)
        self.assertEqual(output, "10\nNULL\n")
    
    def test_set_num_equal_to(self):
        output = check_output(self.cmd + "/input2.txt", shell = True)
        self.assertEqual(output, "2\n0\n1\n")
    
    def test_transaction1(self):
        output = check_output(self.cmd + "/input3.txt", shell = True)
        self.assertEqual(output, "10\n20\n10\nNULL\n")
    
    def test_transaction2(self):
        output = check_output(self.cmd + "/input4.txt", shell = True)
        self.assertEqual(output, "40\nNO TRANSACTION\n")
    
    def test_transaction3(self):
        output = check_output(self.cmd + "/input5.txt", shell = True)
        self.assertEqual(output, "50\nNULL\n60\n60\n")
    
    def test_transaction4(self):
        output = check_output(self.cmd + "/input6.txt", shell = True)
        self.assertEqual(output, "1\n0\n1\n")
