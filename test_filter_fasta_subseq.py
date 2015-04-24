import unittest
import tempfile
from cStringIO import StringIO

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import NucleotideAlphabet

from filter_fasta_subseq import *

valid = StringIO(
"""1\t100\t200
2\t300\t400
3\t500\t600
""")

invalid_start = StringIO(
"""1\tINVALID\t200
2\t300\t400
""")

invalid_end = StringIO(
"""1\t100\tINVALID_END
2\t300\t400
""")

invalid_2rows_only = StringIO(
"""1\t100
2\t300\t400
""")

invalid_id_repeated = StringIO(
"""1\t100\t200
1\t300\t400
""")

class Test_read_id_start_end(unittest.TestCase):
    def test_valid(self):
        id_position = read_id_start_end(valid)
        self.assertTrue(len(id_position), 3)
        self.assertTrue(len(id_position["1"]), 2)
        self.assertTrue(id_position["3"], (500, 600))

    def test_not_numeric(self):
        self.assertRaises(ValueError, read_id_start_end, invalid_start)
        self.assertRaises(ValueError, read_id_start_end, invalid_end)

    def test_incorrect_number_of_columns(self):
        self.assertRaises(ValueError, read_id_start_end, invalid_2rows_only)
        
    def test_no_ids_are_repeated(self):
        self.assertRaises(KeyError, read_id_start_end, invalid_id_repeated)


class Test_extract_subsequence(unittest.TestCase):
    def setUp(self):
        self.record = SeqRecord(Seq("ACGTACGTAAA", NucleotideAlphabet), id="132") 
    
    def test_subseq_in_order(self):
        res = extract_subsequence(self.record, 2, 5)
        self.assertEqual(str(res.seq), "CGTA")
    
    def test_subseq_not_in_order(self):
        res = extract_subsequence(self.record, 5, 2)
        self.assertEqual(str(res.seq), "CGTA")

class Test_extract_subsequences_fasta(unittest.TestCase):
    def setUp(self):
        self.input_fasta = open("input.fasta")
        self.ids = open("seq_id_start_end.dat")

    def create_output(self):
        output_fasta_fh = tempfile.NamedTemporaryFile()
        extract_subsequences_fasta(self.input_fasta, self.ids, output_fasta_fh)
        output_fasta_fh.seek(0)
        return SeqIO.index(output_fasta_fh.name, "fasta")

    def test_output_correct_number_of_seqs(self):
        self.assertEqual(len(self.create_output()), 2)

    def test_output_subseq(self):
        id_seq = self.create_output()
        self.assertEqual(str(id_seq["1"].seq), "CCC")
        self.assertEqual(str(id_seq["3"].seq), "TGCAA")
