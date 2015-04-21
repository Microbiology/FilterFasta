import unittest
from cStringIO import StringIO
from filter_fasta_subseq import *

class Test_read_id_start_end(unittest.TestCase):

    def test_valid(self):
        valid = StringIO("1\t100\t200\n2\t300\t400\n3\t500\t600\n")
        id_position = read_id_start_end(valid)
        self.assertTrue(len(id_position), 3)
        self.assertTrue(len(id_position["1"]), 2)
        self.assertTrue(id_position["3"], (500, 600))

    def test_not_numeric(self):
        invalid_start = StringIO("1\tINVALID\t200\n2\t300\t400\n")
        self.assertRaises(ValueError, read_id_start_end, invalid_start)

        invalid_end = StringIO("1\t100\tINVALID_END\n2\t300\t400\n")
        self.assertRaises(ValueError, read_id_start_end, invalid_end)

    def test_incorrect_number_of_columns(self):
        invalid_2rows_only = StringIO("1\t100\n2\t300\t400\n")
        self.assertRaises(ValueError, read_id_start_end, invalid_2rows_only)
        
    def test_no_ids_are_repeated(self):
        invalid_id_repeated = StringIO("1\t100\t200\n1\t300\t400\n")
        self.assertRaises(KeyError, read_id_start_end, invalid_id_repeated)


class Test_extract_subsequence(unittest.TestCase):
    pass

class Test_extract_subsequence_end_before_start(unittest.TestCase):
    pass

