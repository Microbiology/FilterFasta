import csv

def read_id_start_end(id_start_end_filehandle):
    """ parse file that should have at least 3 columns: id, start, end.
        Returns: 
            map where key is seq id and value is a tuple: start, end.
        Raises: 
            ValueError if file does not have at least 3 columns
            KeyError if seq id seen more than once(maybe a valid use case later)
            ValueError if start, end not a number
    """
    pass

def extract_subsequence(seqRecord, start, end):
    """ extract part of the sequence(start <= end).
        Returns:
            SeqRecord object with the same id and subsequence.
        Raises:
            ValueError if start and/or end position does not exist.
            AssertionError if start is not before end
    """
    assert start <= end
    pass

def extract_subsequence_end_before_start(seqRecord, start, end):
    """ extract part of the sequence(start > end).
        Returns:
            SeqRecord object with the same id and subsequence.
        Raises:
            ValueError if start and/or end position does not exist.
            AssertionError if start is before end
    """
    assert start > end
    pass

def main(input_fasta, id_start_end_file, output_fasta):
    pass

def command_line_args():
    pass

if __name__=="__main__":
    pass
