#!/usr/bin/python
import csv
import argparse
import os

from Bio import SeqIO

def read_id_start_end(id_start_end_filehandle):
    """ parse file that should have at least 3 columns: id, start, end.
        Returns: 
            map where key is seq id and value is a tuple: start, end.
        Raises: 
            ValueError if file does not have at least 3 columns
            KeyError if seq id seen more than once
            ValueError if start, end not a number
    """
    reader = csv.reader(id_start_end_filehandle, delimiter="\t")
    id_pos = {}
    for row in reader:
        if len(row) < 3:
            raise ValueError("File should have 3 columns or more, but found: " + str(row))
        seq_id, start, end = row
        if seq_id in id_pos:
            raise KeyError("Sequence Identifiers should be unique.")
        if not start.isdigit() or not end.isdigit():
            raise ValueError(
                "Start and or End positions should be a number, but found: " + str(row))
        id_pos[seq_id] = (int(start), int(end))
    return id_pos
            

def extract_subsequence(seqRecord, start, end):
    """ extract part of the sequence from start to end if start <= end
        or extract part of the sequence from end to start if end <= start
        Returns:
            SeqRecord object with the same id and subsequence.
        Raises:
            ValueError if start and/or end position does not exist.
    """
    # input is 1-based but python str is 0-based
    subsequence = seqRecord[start - 1 : end] if start <= end else seqRecord[end - 1 : start]
    return subsequence

def extract_subsequences_fasta(input_fasta_fh, id_start_end_fh, output_fasta_fh):
    """ for a given FASTA extract subsequences and save it to output FASTA.
        Params:
            input_fasta_fh, output_fasta_fh input/output FASTA file handles
            id_start_end_fh filehande (see read_id_start_end for format)
    """
    id_to_start_end = read_id_start_end(id_start_end_fh)
    for record in SeqIO.parse(input_fasta_fh, "fasta"):
        if record.id in id_to_start_end:
            start, end = id_to_start_end[record.id]    
            subsequence_record = extract_subsequence(record, start, end)
            SeqIO.write(subsequence_record, output_fasta_fh, "fasta")

def check_file_exists_or_die(file_name):
    if not os.path.isfile(file_name): 
        print "ERROR: file " + file_name + " does not exist: check the file name and path."
        sys.exit(1)

def command_line_args():
    parser = argparse.ArgumentParser(description="Extract subsequences from FASTA.")
    parser.add_argument('-f', required=True, type=str, help="fasta with sequences.")
    parser.add_argument('-o', required=True, type=str, help="output fasta with extracted subsequences.")
    parser.add_argument('-s', required=True, type=str, help="tab-separated file: seq id, start, end for extraction.")
    args = parser.parse_args()
    check_file_exists_or_die(args.f)
    check_file_exists_or_die(args.s)
    return args

if __name__=="__main__":
    args = command_line_args()
    extract_subsequences_fasta(open(args.f), open(args.s), open(args.o, 'w'))

